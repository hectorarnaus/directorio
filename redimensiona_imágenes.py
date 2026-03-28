from pathlib import Path
from PIL import Image
import pillow_avif


INPUT_DIR = Path("provincia")
OUTPUT_DIR = Path("provincia_redimensionado")
TARGET_WIDTH = 800
QUALITY = 75

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

exts = {".jpg", ".jpeg", ".webp", ".avif"}

for path in INPUT_DIR.rglob("*"):
    if path.suffix.lower() not in exts:
        continue

    try:
        with Image.open(path) as img:
            img = img.convert("RGB")

            w, h = img.size
            target_height = round(h * TARGET_WIDTH / w)

            resized = img.resize((TARGET_WIDTH, target_height), Image.Resampling.LANCZOS)

            out_path = OUTPUT_DIR / f"{path.stem}.webp"
            resized.save(out_path, format="WEBP", quality=QUALITY, optimize=True)

            print(f"OK: {path.name} -> {out_path.name}")

    except Exception as e:
        print(f"ERROR: {path.name} -> {e}")
