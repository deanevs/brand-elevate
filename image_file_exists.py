# THIS WORKS SO DON'T F*** WITH IT
#
# Opens the supplier CSV and checks each image column whether the image files
# exist in the supplied directory.
# It iterates over the base directory and sub-dirs
#
# Actions:
#     - supplier filename
#     - supplier dir
#     - image dir
#
# PRINTS to screen images not found

import constants
import csv
import os
import fnmatch


# FILE IO SETUPS
supplier_filename = 'legend life.csv'
#path = 'C:\\Users\\Dean\\Dropbox\\Brand Elevate\\6 Website\\Programming\\Test Files\\'
path = constants.SUPP_PATH
infile = path + supplier_filename
#image_dir = "C:\\Users\\Dean\\OneDrive\\Business\\Supplier Data\\Legend Life - Copy\\Appa File Images"
image_dir = "C:\\wamp64\\www\\brandelevate\\pub\\media\\import\\legend"

res_dir = constants.RESULTS_PATH

def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                return filename

with open(infile,'r',encoding='utf-8') as fin:
    dr = csv.DictReader(fin)
    with open('out.csv','w') as fout:
        writer = csv.writer(fout,delimiter=',')

        for row in dr:
            base = row['product_image_file_name']
            alternate = row['alternate_views_image_file_names']
            group = row['group_image_file_name']
            colour = row['colour_image_file_names']

            base = row['base_image']



            cols = [base,alternate,group,colour]

            img_list = []
            # add all images to a single set
            for col in cols:
                if '|' in col:
                    tmp = col.split('|')
                    for x in tmp:
                        img_list.append(x)
                else:
                    if col:
                        img_list.append(col)
            s = set(img_list)

            # now recursively check in directory path
            for x in range(0,len(s)):
                fn = s.pop()
                if not find_files(image_dir,fn):
                    print (fn)






