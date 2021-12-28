from pathlib import Path
import constants
import csv

"""
Checks that the file exists and if not, prints to screen.

Actions:
    - supplier filename
    - supplier dir
    - image dir

"""


import os

def findInSubdirectory(filename, subdirectory=''):
    if subdirectory:
        path = subdirectory
    else:
        path = os.getcwd()
    for root, dirs, names in os.walk(path):
        if filename in names:
            return os.path.join(root, filename)
    raise 'File not found'


supplier_filename = 'Legend Life.csv'
path = constants.SUPP_PATH
infile = path + supplier_filename

image_dir = "C:\\Users\\Dean\\OneDrive\\Business\\Supplier Data\\Legend Life\\Appa File Images\\"

with open(infile,'r',encoding='utf-8') as fin:
    dr = csv.DictReader(fin)

    for row in dr:
        base = row['product_image_file_name']
        alternate = row['alternate_views_image_file_names']
        group = row['group_image_file_name']
        colour = row['colour_image_file_names']


        cols = [base,alternate,group,colour]
        img_list = []
        for col in cols:
            if '|' in col:
                tmp = col.split('|')
                for x in tmp:
                    img_list.append(x)
            else:
                if col:
                    img_list.append(col)

        s = set(img_list)


        for x in range(0,len(s)):
            filename = s.pop()

            for root,dirs,files in os.walk(image_dir):
                if filename in files:

                    break
                else:
                    print (root + filename)




            # if file:
            #     test_file = Path(image_dir + file)
            #     if not test_file.is_file():
            #         print (file)



        #
        #     if '|' in col:
        #         tmp = col.split('|')
        #         for x in tmp:
        #             img_list.append(x)
        #     else:
        #         img_list.append(col)
        #
        # s = set(img_list)
        #
        #
        # for x in range(0,len(s)):
        #     file = s.pop()
        #     if file:
        #         test_file = Path(image_dir + file)
        #         if not test_file.is_file():
        #             print (file)
