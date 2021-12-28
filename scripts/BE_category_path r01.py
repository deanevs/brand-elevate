# BE_category_path.py
# Utilises the full path CSV file which has one column of full path length
# Dictionary    key     = each category
#               value   = full category path

import csv
from collections import defaultdict
import pandas as pd


df = pd.read_csv("Legend Life.csv")


fd = open("result.txt",'w')

cat_dict = defaultdict(set)
BE_dic = defaultdict(set)
BE_paths = set()

for cell in df.loc[:, 'categorisation']:
    temp = cell.split('|')
    k = temp.pop(0)
    for x in temp:
        #print (x)
        if k not in cat_dict:
            cat_dict[k]=set()
        cat_dict[k].add(x)


for k,v in cat_dict.items():
    fd.write(k + str(v) + '\n')
    print (k,v)

fd.close()



# APPAREL
# APPAREL/BUSINESS
# APPAREL/BUSINESS/ACCESSORIES
# APPAREL/BUSINESS/ACCESSORIES/LADIES
# APPAREL/BUSINESS/ACCESSORIES/MENS


with open("BE Category Full Path - r01.csv",'r') as fd:
    reader = csv.reader(fd)
    ch = set('/')   # delimitter
    k = str     # key
    for row in reader:
        path = 'Default'
        lst = row[0]

        lst_split = lst.split('/')
        lst_len = len(lst_split)
        if lst_len > 0: #then not root


        else:
            key = lst[0]
            path = path + lst[0]

        # # check if string contains / . If not it is the root.
        # if ch & set(cell):  # not root
        #     lst = cell.split('/')  # create list of categories in path
        #     lst_len = len(lst)
        #     first = True  # don't want to read first iteration since root
        #     for x in range(0, lst_len):
        #         path = 'Default'  # resets the path each loop
        #         if first == True:
        #             first = False
        #         else:
        #             k = lst[x].strip()
        #             i = 0
        #             while i <= x:
        #                 path = path + '/' + lst[i].strip()
        #                 i += 1
        #
        # else:  # this is the root
        #     k = cell.strip()
        #     path = path + '/' + k
        # # print(path)
        # # if k not in dic:
        # # dic[k]= paths.update(path)
        # be_dict.update({k: BE_paths.update(path)})


for k,v in be_dict.items():
    print (k,v)

