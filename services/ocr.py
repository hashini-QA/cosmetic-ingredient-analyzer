import pytesseract # a;lows python to call tesseract 
from PIL import Image, ImageFilter, ImageOps

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image: Image.Image) -> str:
    gray = ImageOps.grayscale(image)
    gray = ImageOps.autocontrast(gray)
    gray = gray.filter(ImageFilter.SHARPEN) # to make blur images as sharpen 

    return pytesseract.image_to_string(
        gray,
        config="--oem 3 --psm 6"
    )
