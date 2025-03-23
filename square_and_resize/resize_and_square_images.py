from PIL import Image
from tqdm import tqdm
import os
image_size = 640

file_path = os.path.dirname(os.path.realpath(__file__))
if not file_path == os.getcwd():
    os.chdir(file_path)

def make_square(image_path, output_path):
    image = Image.open(image_path)
    width, height = image.size
    if width == height:
        image.save(output_path)
        return
    elif width > height:
        result = Image.new(image.mode, (width, width), color='white')
        result.paste(image, (0, (width - height) // 2))
    else:
        result = Image.new(image.mode, (height, height), color='white')
        result.paste(image, ((height - width) // 2, 0))
    result.save(output_path)

def resize_image(image_path, output_path, width, height):
    image = Image.open(image_path)
    resized_image = image.resize((width, height), Image.Resampling.LANCZOS)
    resized_image.save(output_path)

a = os.listdir()

for i in tqdm(a, desc="progress"):
    if i[-3:]== "jpg" or i[-3:]== "JPG" or i[-4:]== "jpeg" or i[-3:]== "png":
        make_square(i, i)
        resize_image(i,i,image_size,image_size)
        
        
    

