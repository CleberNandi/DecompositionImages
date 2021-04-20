import sys
import os
from PIL import Image
from pathlib import Path


ROOT_PATH = Path(__file__).resolve().parent

args = sys.argv[1]

if not args:
	print(f"Não foi informado nenhuma imagem.")
	exit()

image_origin_path = os.path.join(ROOT_PATH, 'images', args.split("\\")[-1])

Image_open = Image.open(image_origin_path)

if Image_open.format not in ["PNG", "JPEG", "JPG"]:
	print("Imagem informada não é válida")
	exit()


image_r_path = os.path.join(ROOT_PATH, 'images', 'test-image_r.png')
image_g_path = os.path.join(ROOT_PATH, 'images', 'test-image_g.png')
image_b_path = os.path.join(ROOT_PATH, 'images', 'test-image_b.png')

WIDTH, HEIGHT = Image_open.size

pillow_obj = Image.new("RGB", (WIDTH, HEIGHT))
pixel_set = pillow_obj.load()

# save red image
for col in range(WIDTH):
	for row in range(HEIGHT):
		r, g, b = Image_open.getpixel((col, row))
		pixel_set[col, row] = r, 0, 0

pillow_obj.save(image_r_path)

# save green image
for col in range(WIDTH):
	for row in range(HEIGHT):
		r, g, b = Image_open.getpixel((col, row))
		pixel_set[col, row] = 0, g, 0

pillow_obj.save(image_g_path)

# save blue image
for col in range(WIDTH):
	for row in range(HEIGHT):
		r, g, b = Image_open.getpixel((col, row))
		pixel_set[col, row] = 0, 0, b

pillow_obj.save(image_b_path)
