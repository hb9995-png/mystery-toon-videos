"""캐러셀 이미지(1080x1350 jpg) → 배경음악 있는 릴스(1080x1920): python3 reel.py 이미지폴더 out.mp4 seed"""
import sys, subprocess, os, glob, tempfile
from PIL import Image
src, out = sys.argv[1], sys.argv[2]; seed = sys.argv[3] if len(sys.argv) > 3 else '7'
HERE = os.path.dirname(os.path.abspath(__file__))
imgs = sorted(glob.glob(f'{src}/[0-9][0-9].jpg')); tmp = tempfile.mkdtemp(prefix='yebi_reel_')
for i, p in enumerate(imgs):
    im = Image.open(p).convert('RGB'); bgc = im.getpixel((540, 5))  # 장 배경색으로 위아래를 채운다
    c = Image.new('RGB', (1080, 1920), bgc); c.paste(im, (0, (1920 - 1350) // 2)); c.save(f'{tmp}/{i:02d}.png')
durs = [3.0] + [4.0] * (len(imgs) - 2) + [4.5]; total = sum(durs)
subprocess.run(['python3', f'{HERE}/bgm.py', f'{tmp}/bgm.wav', str(total + 1), seed], check=True)
lst = ''.join(f"file '{tmp}/{i:02d}.png'\nduration {d}\n" for i, d in enumerate(durs)) + f"file '{tmp}/{len(imgs)-1:02d}.png'\n"
open(f'{tmp}/list.txt', 'w').write(lst)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', f'{tmp}/list.txt', '-i', f'{tmp}/bgm.wav',
    '-vf', 'fps=30,format=yuv420p', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-c:a', 'aac', '-b:a', '160k', '-ar', '44100',
    '-af', f'afade=t=out:st={total-1.5}:d=1.5', '-t', str(total), '-movflags', '+faststart', out], check=True)
print(out, total)
