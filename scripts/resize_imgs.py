from PIL import Image
import glob
import tqdm

files_path = glob.glob("assets/img/**/*.png", recursive=True)
files_path = [path for path in files_path if "parallax" not in path]

# Resize image to 900px width while maintaining aspect ratio if the width is greater than 900px
for file in tqdm.tqdm(files_path):
    img = Image.open(file)
    width, height = img.size
    if width > 900:
        img = img.resize((900, int(height * 900 / width)), Image.ANTIALIAS)
        img.save(file, optimize=True, quality=100, method=6, format="WEBP")
    else:
        img.save(file, optimize=True, quality=100, method=6, format="WEBP")
