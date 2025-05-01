from PIL import Image, ImageDraw, ImageFont
import os
import string

os.makedirs("input_images", exist_ok=True)

font = ImageFont.truetype("/home/kalmin/projects/ascii_pic_generator/Orbitron-VariableFont_wght.ttf", 50)

img_size = (128, 128)
bg_color = "white"
text_color = "black"

for letter in string.ascii_uppercase[:5]:
    img = Image.new("RGB", img_size, bg_color)
    draw = ImageDraw.Draw(img)

    bbox = draw.textbbox((0, 0), letter, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((img_size[0] - text_width) // 2, (img_size[1] - text_height) // 2)
    draw.text(position, letter, fill=text_color, font=font)

    img.save(f"input_images/{letter}.png")

print("Alphabet images saved in 'alphabet_images/' folder.")
