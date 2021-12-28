# single attribute collector.py
# _____________________________
# The following is set up for collecting all colours for a supplier
# Tested with Legend - OK 2017-01-10
# Two sets of results
# 1. Set of every individual colour including colours with spaces eg. apple green
# 2. Set of list of colours on each row
# Output results to screen only
#


import pathlib
from BrandElevate_old import mylib

import pandas as pd

col1 = 'colours_available_supplier' # Legend
col2 = 'Colours Available'
col3 = 'colour_tag'
col4 = 'COLOURS'
col5 = 'COLOURS_AVAILABLE'
col6 = 'colours_available_appa'

size1 = 'size'
size2 = 'SIZES'
size3 = 'product_sizes' # Legend
size4 = 'product_item_size'

cat1 = 'categorisation' #BIC , Gloweave, Highcaliber, Legend
cat2 = 'category_ /_ sub category'  # Trends , Elevate , Headwear
cat3 = 'category'   #Biz
cat4 = 'CATEGORY'   #JBs
cat5 = 'joined'     #logoline
cat6 = 'categories' # pen
cat7 = 'Cat1Sub2'   # Texet
cat8 = 'Categories/Short Description'   #Source

single_col_test = col1


out_f = ("out_" + mylib.get_datetime() + ".txt")

regex = "\W+"

set_row = set()
set_colour = set()
pri_col = str
sec_col = str

fd = open("out_" + mylib.get_datetime() + ".txt", 'w')

p = pathlib.WindowsPath("C:\\Users\\Dean\\Dropbox\\Brand Elevate\\6 Website\\7 UTF8 Supplier Data")

for child in p.iterdir():
    print(child)
    df = pd.read_csv(child)
    for cell in df.loc[:, single_col_test]:
        if isinstance(cell, str):
            lst_cell = []
            try:
                lst_cell = cell.split("|")  # ***************************** delimit
                num_products = len(lst_cell)
            except:
                print("Error")
            for colours in lst_cell:  # check for two tone colours
                lst = colours.split(",")    # ***************************** delimit
                if len(lst) > 1:
                    pri_col = lst[0]        # store primary colour
                    sec_col = lst[1]        # and secondary
                    set_colour.add(pri_col) # store both to set also
                    set_colour.add(sec_col)
                else:
                    set_colour.add(colours)
                set_row.add(colours)
            fd.close()

        elif cell in (None, ""):
            print("Empty")

#print (set_row)

for colours in set_row:
    print (colours)

for colours in set_colour:
    print (colours)

# fd = open(out_f, 'w')
#
# for x in set_row:
#     fd.write(str(x) + '\n')
#
# fd.close()