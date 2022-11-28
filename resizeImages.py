from PIL import Image
import os, sys

path = "n/"
dirs = os.listdir(path)


def resize():
    for item in dirs:
        if os.path.isfile(path + item):
            im = Image.open(path + item)
            f, e = os.path.splitext(path + item)
            imResize = im.resize((38,46), Image.ANTIALIAS)
            imResize.save(f + ".jpg", "JPEG", quality=100)


resize()
