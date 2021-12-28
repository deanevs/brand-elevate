# BE_category_path.py
# Utilises the full path CSV file which has one column of full path length
# Dictionary    key     = each category
#               value   = full category path

import csv

dic = {}



with open("BE Category Full Path - r01.csv",'r') as fd:
    reader = csv.reader(fd)

    for row in reader:
        for cell in row:
            k = str

            # check if string contains / . If not it is the root.
            data = cell[0]
            lst = cell.split('/')      # create list of categories in path
            lst_len = len(lst)
            for x in range(0,lst_len-1):
                path = 'Default'
                k = lst[x].strip()
                i = 0
                while i <= x:
                    path = path + '/' + lst[i].strip()
                    i += 1
                if k in dic:
                    dic.update({k:path})
                else:
                    dic[k] = path


for k,v in dic.items():
    print (k)
    print (v)

