#
import csv
from BrandElevate_old import mylib
from BrandElevate_old import constants

import pandas as pd

# get categories for Brand Elevate from CSV file
BE_dic = {}
BE_dic = mylib.get_BE_cat_paths()


# utilises
# constants.LEGEND_BE_CATS


cell_update = 'BE_categories'

# set headers for output file with additional for new categories
headers = ['member_supplier_name', 'membership_number', 'catalogue_name',
       'brand_name', 'label_name', 'appa_product_code', 'product_code',
       'product_name', 'product_code_group', 'categorisation','BE_categories',
       'category__subcategory', 'additional_keywords', 'product_tags',
       'discontinued_stock', 'product_description', 'description_additional',
       'product_features', 'product_materials', 'product_item_size',
       'product_packaging_inner', 'product_image_file_name',
       'alternate_views_image_file_names', 'group_image_file_name',
       'colours_available_appa', 'colours_available_supplier',
       'colour_image_file_names', 'colour_product_codes', 'product_sizes',
       'size_images', 'size_product_code', 'decoration_options_available',
       'decoration_areas', 'indent_only', 'branded', 'custom_field_1',
       'custom_filed_2', 'custom_field_3', 'price_decoration_description',
       'price_by_size', 'price_by_colour', 'decoration_type',
       'price_product_code', 'price_notes', 'MOQ', 'IOQ', 'qty_1', 'price_1',
       'qty_2', 'price_2', 'qty_3', 'price_3', 'qty_4', 'price_4', 'qty_5',
       'price_5', 'qty_6', 'price_6', 'qty_7', 'price_7', 'qty_8', 'price_8',
       'additional_charges_name1', 'additional_charge_value1',
       'additional_charges_notes1', 'additional_charges_name2',
       'additional_charge_value2', 'additional_charges_notes2',
       'carton_height', 'carton_width', 'carton_depth', 'carton_weight',
       'carton_qty', 'carton_cubic', 'carton_notes', 'freight_description',
       'product_URL']

fd = open('OUTPUT-BE Legend Life.csv', 'w',newline='')
writer = csv.DictWriter(fd,fieldnames=headers)
writer.writeheader()

# read in suppliers data
df = pd.read_csv("Legend Life.csv")
for cell in df.loc[:, 'categorisation']:
    lst = cell.split('|')
    #print (lst)
    len_list = len(lst)
    #print (len_list)
    for item in range(len_list-1,-1,-1):
        # get the last item in list
        if lst[item] == 'NEW':
            if lst[item-1] in BE_dic:
                value = BE_dic[lst[item-1]]
                writer.writerow({cell_update:value,'categorisation': cell})
                break
            else:
                writer.writerow({cell_update:'Not in lower level','categorisation': cell})
                break
        elif lst[item] in constants.LEGEND_BE_CATS:
            writer.writerow({cell_update:BE_dic[constants.LEGEND_BE_CATS[lst[item]]], 'categorisation': cell})
            break
        elif lst[item] in BE_dic:
            writer.writerow({cell_update:BE_dic[lst[item]],'categorisation': cell})
            break
        else:
            continue


# *************************************************************




