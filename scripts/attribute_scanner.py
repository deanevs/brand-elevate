# Colours.py
# Iterates through supplier files in a directory and checks the
# colour column for the available colours and saves to a set which
# is saved to text file
#
# Be careful with the delimiter:
# pipe | is most common but some have ,
#
# Check text file in Notepad++ to verify no special characters mixed up
#
# Note the use of the re and regex splits every word i.e. black/grey > black   grey
#
# BIC.csv	            colours_available_supplier	product_sizes
# BIZ.csv	            colour_tag	                size
# Elevate.csv	        colours_available_supplier	product_item_size
# GLOWEAVE.csv	        colours_available_supplier	product_sizes
# Headwear.csv	        colours_available_supplier	NA
# Highcaliber Line.csv	colours_available_supplier	product_sizes
# JBs wear.csv	        COLOURS	                    SIZES
# LogoLine.csv	        COLOURS_AVAILABLE	        NA
# pen australia.csv	    colours_available_supplier	NA
# TEXET - HARVEST   	FUCKED
# The Range 	        colours_available_supplier	NA
# The Source    	    Colours Available	        product_sizes
# Trends Collections    colours_available_appa	    NA
# IT Solutions Caprina		NA

import pandas as pd
import pathlib
import re

# setup display options for debugging
desired_width = 320
pd.set_option('display.width', desired_width)
pd.options.display.max_colwidth = 200

p = pathlib.Path("C:\\Users\\Dean\\Dropbox\\Brand Elevate\\6 Website\\7 UTF8 Supplier Data")

# set to store unique colours only
colour_set = set()
size_set = set()
category_set = set()

# regex will split on all characters
# hence false will split only on |
regex = "\W+"
use_regex = False

do_colour = True
do_size = False
do_categories = False

multi_mode = False


col1 = 'colours_available_supplier'
col2 = 'Colours Available'
col3 = 'colour_tag'
col4 = 'COLOURS'
col5 = 'COLOURS_AVAILABLE'
col6 = 'colours_available_appa'

size1 = 'size'
size2 = 'SIZES'
size3 = 'product_sizes'
size4 = 'product_item_size'

cat1 = 'categorisation' #BIC , Gloweave, Highcaliber, Legend
cat2 = 'category_ /_ sub category'  # Trends , Elevate , Headwear
cat3 = 'category'   #Biz
cat4 = 'CATEGORY'   #JBs
cat5 = 'joined'     #logoline
cat6 = 'categories' # pen
cat7 = 'Cat1Sub2'   # Texet
cat8 = 'Categories/Short Description'   #Source


# astr =
def my_splitter(astr, aset):
    for cell in df.loc[:, astr]:
        if (type(cell) == float):
            continue
        templist = []
        if use_regex == True:
            try:
                #cell = cell.decode()
                templist = re.split(regex, cell)
            except TypeError:
                print("Error: " + astr)
        else:
            try:
                #cell = cell.decode()
                templist = cell.split("|")
            except TypeError:
                print ("Error2: " + astr)
        for x in templist:
            aset.add(x.strip())

def get_cell(astr, aset):
    for cell in df.loc[:,astr]:
        if isinstance(cell, str):
            aset.add(cell)

def save_results(filename, myset):
    fd = open(filename, 'w')
    for x in myset:
        fd.write(str(x) + '\n')
    fd.close()

if multi_mode == True:
    # this will iterate over each file in the directory
    for child in p.iterdir():
        print(child)
        df = pd.read_csv(child)
        # check colours

        if do_colour == True:
            if col1 in df:
                my_splitter(col1, colour_set)
            elif col2 in df:
                my_splitter(col2, colour_set)
            elif col3 in df:
                my_splitter(col3, colour_set)
            elif col4 in df:
                my_splitter(col4, colour_set)
            elif col5 in df:
                my_splitter(col5, colour_set)
            elif col6 in df:
                my_splitter(col6, colour_set)
        # check sizes
        if do_size == True:
            if size1 in df:
                print(size1)
                get_cell(size1, size_set)
            elif size2 in df:
                get_cell(size2, size_set)
            elif size3 in df:
                get_cell(size3, size_set)
            elif size4 in df:
                get_cell(size4, size_set)

        # check categories
        if do_categories == True:
            if cat1 in df:
                my_splitter(cat1, category_set)
            if cat2 in df:
                my_splitter(cat2, category_set)
            elif cat3 in df:
                my_splitter(cat3, category_set)
            elif cat4 in df:
                my_splitter(cat4, category_set)
            elif cat5 in df:
                my_splitter(cat5, category_set)
            elif cat6 in df:
                my_splitter(cat6, category_set)
            elif cat7 in df:
                my_splitter(cat7, category_set)
            elif cat8 in df:
                my_splitter(cat8, category_set)

else:







save_results("colour_list.txt", colour_set)
save_results("size_list.txt", size_set)
save_results("category_list.txt", category_set)

