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




supplier_filename = 'The Range - The Range.csv'
path = constants.SUPP_PATH
infile = path + supplier_filename


with open(infile,'r',encoding='utf-8') as fin:
    dr = csv.DictReader(fin)
    cat_set = set()
    catpath_set = set()
    for row in dr:
        cats = row['category_ /_sub category']

        catlist = cats.split('|')
        length = len(catlist)

        for n in range(0,length):
            #print (catlist[n])
            if not catlist[n] in cat_set:
                catpath_set.update([catlist[n].strip()])
            tmp = catlist[n].split('/')
            lengthtmp = len(tmp)
            for n in range(0,lengthtmp):
                if not tmp[n] in cat_set:
                    cat_set.update([tmp[n].strip()])



    for s in catpath_set:
        print (s)
    print ('*****')
    for s in cat_set:
        print (s)