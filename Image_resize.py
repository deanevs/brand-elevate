#


from PIL import Image
import os,sys
import pathlib
import glob, os
import constants

#path = "C:\\Users\\Dean\\Test Out Files\\Test Images\\"
path = "C:\\Users\\Dean\\OneDrive\\Business\\Supplier Data\\Legend Life - Copy\\Appa File Images\\"
infile = path


size_thumb = (128, 128)
txt_thumb = '_thumb'
size_small = (470,470)
txt_small = '_small'


for infile in os.listdir(path=path):
    if infile.endswith('.jpg'):

        # print (infile)
        # img = Image.open(path + infile)
        # print(img.format, img.size, img.mode)

        outfile_thumb = os.path.splitext(path + infile)[0] + txt_thumb + '.jpg'
        if infile != outfile_thumb:
            try:
                im = Image.open(path + infile)
                im.thumbnail(size_thumb)
                im.save(outfile_thumb, "JPEG")
            except IOError:
                print("cannot create thumbnail for", infile)

        outfile_small = os.path.splitext(path + infile)[0] + txt_small + '.jpg'
        if infile != outfile_small:
            try:
                im = Image.open(path + infile)
                im.thumbnail(size_small)
                im.save(outfile_small, "JPEG")
            except IOError:
                print("cannot create small for", infile)
