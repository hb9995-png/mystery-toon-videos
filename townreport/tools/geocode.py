import json, sys, time, urllib.request, urllib.parse
def station(name, near_dong=None):
    q=urllib.parse.quote(name)
    url=f"https://nominatim.openstreetmap.org/search?format=json&limit=15&countrycodes=kr&q={q}"
    r=json.load(urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"townreport/0.1"}),timeout=20))
    time.sleep(1.1)
    rail=[x for x in r if x['class'] in('railway','public_transport') and x['type'] in('station','stop_position','platform','stop_area')]
    if near_dong: rail=[x for x in rail if near_dong in x['display_name']] or rail
    x=(rail or r)[0]; return float(x['lat']),float(x['lon']),x['class'],x['type'],x['display_name'][:60]
if __name__=='__main__':
    for n in sys.argv[1:]: print(n, station(n))
