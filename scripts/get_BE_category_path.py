# BE_category_path.py
# Utilises the full path CSV file which has one column of full path length
# Dictionary    key     = each category
#               value   = full category path

import csv
import constants
import mylib


path_results = constants.RESULTS_PATH
path_files = constants.REF_PATH

fin = path_files + 'BE Codazon Category Paths.csv'

category_dic = {}


with open(fin,'r') as fd:
    reader = csv.reader(fd)
    category_dic = mylib.get_categories(reader)


# test
for k,v in category_dic.items():
    print (k,v)

