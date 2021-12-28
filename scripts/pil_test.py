from PIL import Image
import os,sys
import pathlib

import constants

path = "C:\\Users\\Dean\\Test Out Files\\Test Images\\"
path = "C:\\Users\\Dean\\OneDrive\\Business\\Supplier Data\\Legend Life\\Appa File Images\\"
infile = path


size_thumb = (100, 100)
txt_thumb = '_thumb'
size_small = (470,470)
txt_small = '_small'


for fn in os.listdir(path=path):
    print (fn)
    img = Image.open(path + fn)
    print(img.format, img.size, img.mode)

    outfile_thumb = os.path.splitext(path + fn)[0] + txt_thumb + '.jpg'
    if fn != outfile_thumb:
        try:
            im = Image.open(path + fn)
            im.thumbnail(size_thumb)
            im.save(outfile_thumb, "JPEG")
        except IOError:
            print("cannot create thumbnail for", infile)

    outfile_small = os.path.splitext(path + fn)[0] + txt_small + '.jpg'
    if fn != outfile_small:
        try:
            im = Image.open(path + fn)
            im.thumbnail(size_small)
            im.save(outfile_small, "JPEG")
        except IOError:
            print("cannot create small for", infile)
