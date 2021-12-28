# BE_category_path.py
# Utilises the full path CSV file which has one column of full path length
# Dictionary    key     = each category
#               value   = full category path

import csv


dic = {}
catset = set()

with open("BE Category Full Path - r01.csv",'r') as fd:
    reader = csv.reader(fd)

    for row in reader:
        ch = set('/')
        k = str
        for cell in row:
            path = 'Default'
            # check if string contains / . If not it is the root.
            if ch & set(cell):  # not root
                lst = cell.split('/')      # create list of categories in path
                lst_len = len(lst)
                first = True            # don't want to read first iteration since root
                for x in range(0, lst_len):
                    path = 'Default'        # resets the path each loop
                    if first == True:
                        first = False
                    else:
                        k = lst[x].strip()
                        i = 0
                        while i <= x:
                            path = path + '/' + lst[i].strip()
                            i += 1

            else:      # this is the root
                k = cell.strip()
                path = path + '/' + k
            print (path)
            #if k not in dic:
            #dic[k]= paths.update(path)
            dic.update({k:catset.update(path)})

for k,v in dic.items():
    print (k,v)

