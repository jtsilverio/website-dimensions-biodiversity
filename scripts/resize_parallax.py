from PIL import Image
import glob
import tqdm

files_path = glob.glob("assets/img/parallax/**/*.png", recursive=True)

for file in tqdm.tqdm(files_path):
    img = Image.open(file)
    # width, height = img.size
    # if width > 900:
    #     img = img.resize((1440, int(height * 1440 / width)), Image.ANTIALIAS)
    #     img.save(file, optimize=True, quality=50)
    # else:
    img.save(file, optimize=True, quality=95, method=6, format="WEBP")