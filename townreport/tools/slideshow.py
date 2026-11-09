"""캐러셀 8장 → 음악 있는 릴스(1080x1920): python3 slideshow.py 이미지폴더 out.mp4 [seed]"""
import sys, subprocess, os, glob
from PIL import Image
src, out = sys.argv[1], sys.argv[2]; seed = sys.argv[3] if len(sys.argv) > 3 else '7'
imgs = sorted(glob.glob(f'{src}/*.jpg')); tmp = f'build/ss_{os.path.basename(src)}'; os.makedirs(tmp, exist_ok=True)
PAPER = (250, 246, 238)
for i, p in enumerate(imgs):
    c = Image.new('RGB', (1080, 1920), PAPER); im = Image.open(p).convert('RGB')
    c.paste(im, (0, (1920 - 1350) // 2)); c.save(f'{tmp}/{i:02d}.png')
durs = [3.5] + [3.2] * (len(imgs) - 2) + [4.5]; total = sum(durs)
subprocess.run(['python3', 'bgm.py', f'{tmp}/bgm.wav', str(total + 1), seed], check=True)
lst = ''.join(f"file '{os.path.abspath(tmp)}/{i:02d}.png'\nduration {d}\n" for i, d in enumerate(durs)) + f"file '{os.path.abspath(tmp)}/{len(imgs)-1:02d}.png'\n"
open(f'{tmp}/list.txt', 'w').write(lst)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', f'{tmp}/list.txt', '-i', f'{tmp}/bgm.wav',
    '-vf', 'fps=30,format=yuv420p', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-c:a', 'aac', '-b:a', '160k',
    '-af', f'afade=t=out:st={total-1.5}:d=1.5', '-t', str(total), '-movflags', '+faststart', out], check=True)
print(out, total)
