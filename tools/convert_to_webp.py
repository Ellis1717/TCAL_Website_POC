from PIL import Image
import os

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
ASSETS = str(ROOT / "assets")
IMAGES = [
    "TCAL_group_image_2.png",
    "TCAL_group_image_1.png",
]
# widths to generate (px)
WIDTHS = [480, 800, 1200]
QUALITY = 80

os.makedirs(ASSETS, exist_ok=True)

for img_name in IMAGES:
    src_path = os.path.join(ASSETS, img_name)
    if not os.path.exists(src_path):
        print(f"Source missing: {src_path}")
        continue
    im = Image.open(src_path).convert('RGB')
    orig_w, orig_h = im.size
    print(f"Processing {img_name} ({orig_w}x{orig_h})")
    base, _ = os.path.splitext(img_name)
    for w in WIDTHS:
        if w >= orig_w:
            # skip upscaling, save full-size as largest
            w_to_use = orig_w
        else:
            w_to_use = w
        h = int((w_to_use / orig_w) * orig_h)
        if w_to_use == orig_w:
            out = im
        else:
            out = im.resize((w_to_use, h), Image.LANCZOS)
        out_name = f"{base}-{w_to_use}w.webp"
        out_path = os.path.join(ASSETS, out_name)
        out.save(out_path, format='WEBP', quality=QUALITY, method=6)
        print(f"  wrote {out_name}")
    # also write a same-dimension webp file as a progressive fallback (largest)
    full_out = os.path.join(ASSETS, f"{base}.webp")
    im.save(full_out, format='WEBP', quality=QUALITY, method=6)
    print(f"  wrote {base}.webp")

print("Done")
