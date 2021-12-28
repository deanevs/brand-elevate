
"""
# INSTRUCTIONS
# The supplier file name is changed below and the path should be the same.
# That is it hopefully.
# Two files are produced one for the Magento import and the other for advanced pricing


Notes:
    - the category dictionary matching is case sensitive.  Currently all are upper case

"""

import csv
import legend
import constants
import mylib
import re
import pandas as pd



# setup display options for debugging
desired_width = 420
pd.set_option('display.width', desired_width)
pd.options.display.max_colwidth = 200

supplier_filename = 'Legend Life.csv'

# file IO setup
test_path = "C:\\Users\\Dean\\Dropbox\\Brand Elevate\\6 Website\\Programming\\Test Files\\"
in_path = constants.SUPP_PATH
out_path = constants.RESULTS_PATH

infile = in_path + supplier_filename
outfile = out_path + supplier_filename + "-" + mylib.get_datetime() + ".csv"


# Opens supplier file, retrieves its headers and adds BE cols to end
# returns list of headers
def get_infile_headers():
    with open(infile,'r',encoding='utf-8') as fin:
        dr = csv.DictReader(fin, delimiter=',')
        lst = dr.fieldnames
    return (lst)

# Write in dictionary mapping values to magento import
# New line at end so all writes have to be done in one time
# Return = nothing
def fill_row(dw_obj= csv.DictWriter, dic= constants.MAGENTO_IMPORT_DIC):
    dw_obj.writerow(dic)    # writes a new row in the output import file
    return

# Helper to set values in the magento dictionary before writing
def set(k,v):
    constants.MAGENTO_IMPORT_DIC[k] = v
    return

# Helper for setting the dictionary for writing to Advanced Pricing
def set2(k,v):
    constants.ADV_PRICING_DIC[k] = v
    return
# Helper to map values directly through to the magento import dictionary
# from the supplier file
# dic1 = import, dic2 = supplier
# Return = nothing
def transfer_values(dic1=legend.LEGEND_MAP, dic2=constants.MAGENTO_IMPORT_DIC,dr = csv.DictReader):
    for k in dic1:
        dic2[dic1[k]] = row[k]
    return

# Helper to maps fields in the import file that have the same value.
# e.g. product_name is also the Meta Title
# def map_eq_fields(imp=constants.MAGENTO_IMPORT_DIC,map=constants.SET_EQUAL_FIELDS_DIC):
#     for key in map:
#         imp[key] = imp[map[key]]
#     return

# Helper to change each product name into the url format
# formats to lower case and replaces " " with "-"
# Return url_name as string
def url_key_format(s=str):
    in_str = s.lower()
    return in_str.replace(' ', '-')


# formats output of list/dictionary into clean string for Magento
def fmt(lst=[]):
    out_str = str

    # length = len(lst)
    # for n in range(0,length):
    #     out_str = out_str + lst[n] + '|'
    in_list = str(lst)

    ch_remove = str.maketrans("", "", "['][\"]{}")
    tmp = in_list.translate(ch_remove)
    if ',' in tmp:
        tmp = tmp.replace(',', '|')
    if '| ' in tmp:
        tmp = tmp.replace('| ','|')
    return tmp

#
def get_col_image_dic(col,img=[]):
    image_list = img.split('|')
    for col_img in image_list:
        col_of_img = col_img[col_img.find("(") + 1:col_img.find(")")]
        # now convert to BE

# Helper for debugging
# prints dictionary
def print_dic(dic={}):
    for k,v in dic.items():
        print (k,v)

# formats and updates the path of the images folder
def update_path(s=str):
    fn = format_filename(s)
    #fn = '/legend/' + fn
    return fn

# Don't think this is used
def remove_brackets(s):
    translator = str.maketrans('(,)', '_-_')
    return s.translate(translator)


# used for formatting the image filenames since Magento doesn't like (,)
def format_filename(fn=str):
    reg1 = re.compile(r'\(')
    reg2 = re.compile('\)')
    reg3 = re.compile(',')
    f1 = re.sub(reg1,'_',fn)
    f2 = re.sub(reg2,'',f1)
    f3 = re.sub(reg3,'_',f2)
    return f3

"""
# *****************************************************
# MAIN PROGRAM
# *****************************************************
"""


# setup dictionaries
category_paths_dic = mylib.get_BE_category_paths()
#


with open(infile,'r',encoding='utf8') as fin:
    dr = csv.DictReader(fin)

    with open(outfile,'w',encoding='utf8',newline='') as fout:
        dw = csv.DictWriter(fout, delimiter=',', fieldnames=constants.MAGENTO_HEADERS, extrasaction='ignore')
        dw.writeheader()

        for row in dr:


            categorisation = row['categorisation']
            category__subcategory = row['category__subcategory']
#
            """
            ********DO CATEGORIES**********
            """
            print (categorisation)
            category_list = []
            num_categories = 0
            category_return = []
            temp_list = []
            if categorisation:  # check cell not empty
                category_list = categorisation.split('|')    # JACKETS|WEATHER/ACTIVEWEAR -> JACKETS , WEATHER/ACTIVEWEAR
                num_categories = len(category_list)         # length = 2

                for level in range(num_categories -1, -1, -1):  # start from tail of path
                    cat_item = category_list[level]
                    if level == 0:
                        break
                    #     if cat_item in category_paths_dic[cat_item]:
                    #         temp_list.append(cat_item)
                    #         break
                    if cat_item == 'NEW':
                        temp_list.append('Default Category/New')
                        #continue
                    elif cat_item in constants.CAT_DOUBLES:
                        continue
                        # cat_next = category_list[level-1]
                        # print(categorisation)
                        # if cat_next in constants.LEGEND_BE_CATS:
                        #
                        #     tmp = category_paths_dic[constants.LEGEND_BE_CATS[cat_next]]
                        #     tmp = tmp + '/' + cat_item
                        #     temp_list.append(tmp.strip())
                        #     #break
                        #     #temp_list.append(category_paths_dic[constants.LEGEND_BE_CATS[cat_item]]+'/' + cat_item)
                        #     #continue    # need to go deeper later
                        # elif cat_next in category_paths_dic:
                        #     tmp = str(category_paths_dic[cat_next])
                        #     tmp = tmp + '/' + cat_item
                        #     temp_list.append(tmp.strip())
                            #break
                            #continue

                    elif cat_item in constants.LEGEND_BE_CATS:       # a few mapped since not in BE
                        temp_list.append(category_paths_dic[constants.LEGEND_BE_CATS[cat_item]])
                        #break
                        #continue
                    elif cat_item in category_paths_dic:
                        temp_list.append(str(category_paths_dic[cat_item]).strip())
                        #break
                        #continue
            category_return = fmt((temp_list))   #
            #print (category_return)
            #print ()

