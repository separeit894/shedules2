import os

import fitz  # PyMuPDF
from PIL import Image


path = "shedules"

def converter():
    for el in os.listdir(path):
        print(el)
        pdf_path = f"shedules/{el}"
        print(pdf_path)
        images = convert_from_path(pdf_path)
        for i, image in enumerate(images):
            image.save(f"photo/page{i}.png", "PNG")
            print(f"файл № {i} конвертирован")



