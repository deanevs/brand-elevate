# single attribute collector r01.py
# _____________________________
# The following is set up for collecting all colours for a supplier
# Tested with Legend - OK 2017-01-10
# Two sets of results
# 1. Set of every individual colour including colours with spaces eg. apple green
# 2. Set of list of colours on each row
# Output:
# results to screen and to file by setting to true
#


import pathlib
from BrandElevate_old import mylib
from BrandElevate_old import  constants

import pandas as pd

# CONSTANTS
COL1 = 'colours_available_supplier' # Legend
COL2 = 'Colours Available'
COL3 = 'colour_tag'
COL4 = 'COLOURS'
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

# ****** SETUP *******
COL_HEADER = COL1
write_to_file = False        # out-legend life-2017-01-10-06-05-03.txt
second_delimit = False       # ['red','blue,green','white'] splits the blue,green too
# ********************
# file IO setup
in_path = constants.SUPP_PATH
out_path = constants.RESULTS_PATH
infile = in_path + supplier_name + ".csv"
outfile = out_path + supplier_name + "-" + mylib.get_datetime() + ".csv"



# GLOBALS
set_row = set()
set_colour = set()
p = pathlib.WindowsPath("C:\\Users\\Dean\\Dropbox\\Brand Elevate\\6 Website\\7 UTF8 Supplier Data")

# Helper Functions
def get_supplier(s):
    lst = s.split('\\')
    length = len(lst)
    result = lst[length - 1]
    lst1 = result.split('.')
    return lst1[0]


# MAIN
for child in p.iterdir():
    supplier = get_supplier(str(child))
    df = pd.read_csv(child)
    for cell in df.loc[:, COL_HEADER]:
        if isinstance(cell, str):
            lst_cell = []
            try:
                lst_cell = cell.split("|")  # ***************************** delimit
                num_products = len(lst_cell)
            except:
                print("Error")

            for colours in lst_cell:  # check for two tone colours
                set_row.add(colours)
                if second_delimit == True:
                    lst = colours.split(",")  # ***************************** delimit
                    if len(lst) > 1:
                        pri_col = lst[0]  # store primary colour
                        sec_col = lst[1]  # and secondary
                        set_colour.add(pri_col)  # store both to set also
                        set_colour.add(sec_col)
                    else:
                        set_colour.add(colours)


        elif cell in (None, ""):
            print("Empty")

#print (set_row)

for colours in set_row:
    print (colours)

for colours in set_colour:
    print (colours)

if write_to_file == True:
    out_f = open("out-" + supplier +"-" + mylib.get_datetime() + ".txt", 'w', newline='\n')
    for x in set_row:
        out_f.write(str(x) + '\n')
    for x in set_colour:
        out_f.write(str(x) + '\n')
    out_f.close()