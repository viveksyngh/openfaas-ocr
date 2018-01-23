try:
    import Image
except ImportError as e:
    from PIL import Image

import pytesseract
import urllib.request
import os
from uuid import uuid4
from urllib.parse import urlparse
from os.path import splitext
ALLOWED_IMAGE_TYPE = [".jpeg", ".png", ".jpg"]

def get_ext(url):
    parsed = urlparse(url)
    _, ext = splitext(parsed.path)
    return ext

def save_image_local(url):
    ext = get_ext(url)
    local_file_path = "/tmp/" + str(uuid4()) + ext
    urllib.request.urlretrieve(url, local_file_path)
    return local_file_path

def handle(url):
    if get_ext(url) not in ALLOWED_IMAGE_TYPE:
        raise Exception("Invalid Image file type")
    file_path = save_image_local(url)
    img = Image.open(file_path)
    text = pytesseract.image_to_string(img, lang='eng')
    os.remove(file_path)
    print(text)

