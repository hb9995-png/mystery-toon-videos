import json, math, io, sys, os, time, urllib.request
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
TILE=256
def ll2px(lon,lat,z):
    n=2**z*TILE; x=(lon+180)/360*n
    s=math.sin(math.radians(lat)); y=(0.5-math.log((1+s)/(1-s))/(4*math.pi))*n
    return x,y
def get_tile(z,x,y,cache):
    p=f"{cache}/{z}_{x}_{y}.png"
    if not os.path.exists(p):
        req=urllib.request.Request(f"https://tile.openstreetmap.org/{z}/{x}/{y}.png",headers={"User-Agent":"dongne-report-sample/0.1 (personal content test)"})
        open(p,'wb').write(urllib.request.urlopen(req,timeout=30).read()); time.sleep(0.2)
    return Image.open(p).convert('RGB')
def build(adm_nm, out_prefix, W=1080, H=1240, pad=0.06):
    d=json.load(open('/home/claude/dongne/data/dong.json'))
    f=[f for f in d['features'] if f['properties']['adm_nm']==adm_nm][0]
    g=f['geometry']; polys=g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
    pts=[p for poly in polys for ring in poly for p in ring]
    lons=[p[0] for p in pts]; lats=[p[1] for p in pts]
    for z in range(int(os.environ.get("ZMAX","17")),11,-1):
        x0,y1=ll2px(min(lons),min(lats),z); x1,y0=ll2px(max(lons),max(lats),z)
        if (x1-x0)<=W*(1-2*pad) and (y1-y0)<=H*(1-2*pad): break
    cx,cy=(x0+x1)/2,(y0+y1)/2; L,T=cx-W/2,cy-H/2
    cache='/home/claude/dongne/data/tiles'; os.makedirs(cache,exist_ok=True)
    img=Image.new('RGB',(W,H))
    for tx in range(int(L//TILE),int((L+W)//TILE)+1):
        for ty in range(int(T//TILE),int((T+H)//TILE)+1):
            img.paste(get_tile(z,tx,ty,cache),(int(tx*TILE-L),int(ty*TILE-T)))
    img.save(f'{out_prefix}_raw.png')
    # restyle: soft warm paper look
    g2=ImageOps.grayscale(img); g2=ImageEnhance.Contrast(g2).enhance(0.75)
    styled=ImageOps.colorize(g2,black=(70,74,88),white=(250,246,238))
    styled.save(f'{out_prefix}_map.png')
    proj=lambda lon,lat:(ll2px(lon,lat,z)[0]-L, ll2px(lon,lat,z)[1]-T)
    rings=[[proj(*p) for p in poly[0]] for poly in polys]
    json.dump({'z':z,'L':L,'T':T,'rings':rings},open(f'{out_prefix}_geo.json','w'))
    print('zoom',z)
if __name__=='__main__': build(sys.argv[1],sys.argv[2])
