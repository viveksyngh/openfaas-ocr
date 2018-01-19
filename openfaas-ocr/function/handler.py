try:
    import Image
except ImportError as e:
    from PIL import Image

import pytesseract

def handle(st):
    im = Image.open("sample1.jpg")
    text = pytesseract.image_to_string(im, lang='eng')
    print(text)
    return text

