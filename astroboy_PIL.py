import os

from PIL import Image

os. chdir(r"D:\temp\Astro Boy Volume 15 - Osamu Tezuka\Astro_Boy_v15")
base_name = "Astroboy-v15-p"

with Image.open("Astroboy-v15-p003.png") as im:
    wdth, hght = im.size

for i in range(3,118):
    im = Image.open(f"{base_name}{i:03d}.png")
    left = im.crop((0,0, 1127, hght))
    right = im.crop((1127, 0, wdth, hght))
    left.save(f"out\\{base_name}{i:03d}0.png")
    right.save(f"out\\{base_name}{i:03d}5.png")
    im.close()