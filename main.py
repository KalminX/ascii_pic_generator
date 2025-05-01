from PIL import Image
import uuid
import sys
import os

ASCII_CHARS = ".@#*+=-:."

def pixel_to_ascii(pixel):
    return ASCII_CHARS[pixel // 32]

def grayscale_image(image):
    return image.convert("L")

def resize_image(image, new_width=50):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def image_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ''.join([pixel_to_ascii(pixel) for pixel in pixels])
    
    ascii_str_len = len(ascii_str)
    ascii_str = [ascii_str[index:index + 50] for index in range(0, ascii_str_len, 50)]
    return "\n".join(ascii_str)


def main(image_path):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        sys.exit()

    image = resize_image(image)
    
    image = grayscale_image(image)
    
    ascii_art = image_to_ascii(image)
    

    filename = f"output_ascii/ascii_art_{uuid.uuid4().hex}.txt"
    with open(filename, "w") as f:
        f.write(ascii_art)


if __name__ == "__main__":
    output_folder = "output_ascii"
    input_folder = "input_images"
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(input_folder, exist_ok=True)


    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(input_folder, filename)
            main(image_path)

    print("✅ All images converted to ASCII text files.")
