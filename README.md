```markdown
# 🖼️ Image to ASCII Art Generator

A simple Python tool that converts images into ASCII art! It loops through all images in the `input_images/` folder and outputs ASCII text versions into the `output_ascii/` folder.

---

## 📦 Features

- Converts all images in a folder to `.txt` ASCII files
- Automatically resizes and grayscales images
- Clean, readable output using a customizable ASCII charset

---

## ⚙️ Setup

1. **Install dependencies**

Make sure you have [Pillow](https://python-pillow.org/) installed:

```bash
pip install pillow
```

2. **Generate Sample Images (Optional)**

Run this to create test alphabet images:

```bash
python3 gen.py
```

This will create some sample images in the `input_images/` folder.

3. **Generate ASCII Art**

Run the main script:

```bash
python3 main.py
```

This will convert all images from `input_images/` into ASCII `.txt` files in the `output_ascii/` folder.

---

## 📁 Folder Structure

```
├── gen.py            # Generates sample images (A-Z)
├── main.py           # Main converter script
├── input_images/     # Put your source images here
├── output_ascii/     # ASCII text files will be saved here
├── README.md
```

---

## 🧪 Example Output

Example image (`A.png`) will be converted to:

```
@@@@@@@ooo**==__~~
@@@@oo**==__~~''  
@@@o*-=_~~'       
...
```

---

## ✨ Notes

- Only `.png`, `.jpg`, `.jpeg` files are processed.
- ASCII resolution and detail can be tweaked by adjusting the image width in `main.py`.

---

## 🧠 Credits

Made with Python 🐍 and Pillow 🖼️  
By [Kalmin]
```
