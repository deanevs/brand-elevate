"""
# INSTRUCTIONS
# The supplier file name is changed below and the path should be the same.
# That is it hopefully.
# Two files are produced one for the Magento import and the other for advanced pricing

R01 - 21-01-2017
Category
- changed category analyis to include child paths also
- category analysis to include 'NEW'
- fmt changed to remove " and space after |
Image
- changed the format helper to rename files according to thumb etc

Product_name
- unique ID added to duplicate names for url-key

Notes:
    - the category dictionary matching is case sensitive.  Currently all are upper case

"""
import csv
import legend
import constants
import mylib
import re
import pandas as pd
import itertools
import random






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
outfile2 = out_path + supplier_filename + 'adv-price' + mylib.get_datetime() + ".csv"

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

    in_list = str(lst)
    out_str = str
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
# NOW NEED TO CHANGE NAME ALSO
def update_path(s=str,img_type=str):
    rtn = str
    fn = format_filename(s)     # rename
    if img_type == 'base':
        rtn = fn
    elif img_type == 'small':
        rtn = fn.replace(".","_small.")
    elif img_type == 'thumb':
        rtn = fn.replace(".","_thumb.")
    elif img_type == 'swatch':
        rtn = fn.replace(".", "_thumb.")
    else:
        #print ("SOMETHING WENT WRONG!!!   -   " + fn)
        rtn = fn
    #print (rtn)
    return rtn

# Don't think this is used
def remove_brackets(s):
    translator = str.maketrans('(,)', '_-_')
    return s.translate(translator)


# used for formatting the image filenames since Magento doesn't like (,)
def format_filename(fn=str):
    reg1 = re.compile(r'\(')
    reg2 = re.compile('\)')
    reg3 = re.compile(',')
    reg4 = re.compile(' ')
    f1 = re.sub(reg1,'_',fn)
    f2 = re.sub(reg2,'',f1)
    f3 = re.sub(reg3,'_',f2)
    f4 = re.sub(reg4,'_',f3)
    return f4


def random_permutation(iterable, r=None):
    "Random selection from itertools.permutations(iterable, r)"
    pool = tuple(iterable)
    r = len(pool) if r is None else r
    return tuple(random.sample(pool, r))

"""
# *****************************************************
# MAIN PROGRAM
# *****************************************************
"""


# setup dictionaries
category_paths_dic = mylib.get_BE_category_paths()

#supplier_headers = get_infile_headers()

with open(infile,'r',encoding='utf8') as fin:
    dr = csv.DictReader(fin)

    fout1 = open(outfile2,'w',encoding='utf-8',newline='')
    dw1 = csv.DictWriter(fout1,delimiter=',',fieldnames=constants.ADV_PRICING_HEADERS)
    dw1.writeheader()

    with open(outfile,'w',encoding='utf8',newline='') as fout:
        dw = csv.DictWriter(fout, delimiter=',', fieldnames=constants.MAGENTO_HEADERS, extrasaction='ignore')
        dw.writeheader()
        name_list = []


        for row in dr:
            # map through all values that do not change
            # for key in legend.LEGEND_MAP:
            #     constants.MAGENTO_IMPORT_DIC[legend.LEGEND_MAP[key]] = row[key]

            member_supplier_name = row['member_supplier_name'],
            membership_number = row['membership_number'],
            catalogue_name = row['catalogue_name'],
            brand_name = row['brand_name'],
            label_name = row['label_name'],
            appa_product_code = row['appa_product_code'],
            product_code = row['product_code'],
            product_name = row['product_name'],
            product_code_group = row['product_code_group'],
            category_subcategory = row['category_ /_sub category'],
            additional_keywords = row['additional_keywords'],
            product_tags = row['product_tags'],
            discontinued_stock = row['discontinued_stock'],
            product_description = row['product_description'],
            description_additional = row['description_additional'],
            product_features = row['product_features'],
            product_materials = row['product_materials'],
            product_item_size = row['product_item_size'],
            product_packaging_inner = row['product_packaging_inner'],
            product_image_file_name = row['product_image_file_name'],
            alternate_views_image_file_names = row['alternate_views_image_file_names'],
            group_image_file_name = row['group_image_file_name'],
            colours_available_appa = row['colours_available_appa'],
            colours_available_supplier = row['colours_available_supplier'],
            colour_image_file_names = row['colour_image_file_names'],
            colour_product_codes = row['colour_product_codes'],
            product_sizes = row['product_sizes'],
            size_images = row['size_images'],
            size_product_code = row['size_product_code'],
            decoration_options_available = row['decoration_options_available'],
            decoration_areas = row['decoration_areas'],
            indent_only = row['indent_only'],
            branded = row['branded'],
            custom_field_1 = row['custom_field_1'],
            custom_field_2 = row['custom_field_2'],
            custom_field_3 = row['custom_field_3'],
            price_decoration_description = row['price_decoration_description'],
            price_by_size = row['price_by_size'],
            price_by_colour = row['price_by_colour'],
            decoration_type = row['decoration_type'],
            price_product_code = row['price_product_code'],
            price_notes = row['price_notes'],
            MOQ = row['MOQ'],
            IOQ = row['IOQ'],
            qty_1 = row['qty_1'],
            price_1 = row['price_1'],
            qty_2 = row['qty_2'],
            price_2 = row['price_2'],
            qty_3 = row['qty_3'],
            price_3 = row['price_3'],
            qty_4 = row['qty_4'],
            price_4 = row['price_4'],
            qty_5 = row['qty_5'],
            price_5 = row['price_5'],
            qty_6 = row['qty_6'],
            price_6 = row['price_6'],
            qty_7 = row['qty_7'],
            price_7 = row['price_7'],
            qty_8 = row['qty_8'],
            price_8 = row['price_8'],
            additional_charges_name1 = row['additional_charges_name1'],
            additional_charge_value1 = row['additional_charge_value1'],
            additional_charges_notes1 = row['additional_charges_notes1'],
            additional_charges_name2 = row['additional_charges_name2'],
            additional_charge_value2 = row['additional_charge_value2'],
            additional_charges_notes2 = row['additional_charges_notes2'],
            carton_height = row['carton_height'],
            carton_width = row['carton_width'],
            carton_depth = row['carton_depth'],
            carton_weight = row['carton_weight'],
            carton_qty = row['carton_qty'],
            carton_cubic = row['carton_cubic'],
            carton_notes = row['carton_notes'],
            freight_description = row['freight_description'],
            product_URL = row['product_URL'],

            """
            *************DO ADVANCED PRICING *****************
            """
            tier_price = False
            num_tiers = 0
            qty_arr = []
            price_arr = []

            if qty_1 and price_1:
                num_tiers += 1
                qty_arr.append(qty_1)
                price_arr.append(price_1)
                if qty_2 and price2:
                    num_tiers += 1
                    qty_arr.append(qty_2)
                    price_arr.append(price_2)
                    tier_price = True
                    if qty_3 and price_3:
                        num_tiers += 1
                        qty_arr.append(qty_3)
                        price_arr.append(price_3)
                        if qty_4 and price_4:
                            num_tiers += 1
                            qty_arr.append(qty_4)
                            price_arr.append(price_4)
                            if qty_5 and price_5:
                                num_tiers += 1
                                qty_arr.append(qty_5)
                                price_arr.append(price_5)
                                if qty_6 and price_6:
                                    num_tiers += 1
                                    qty_arr.append(qty_6)
                                    price_arr.append(price_6)
                                    if qty_7 and price_7:
                                        num_tiers += 1
                                        qty_arr.append(qty_7)
                                        price_arr.append(price_7)
                                        if qty_8 and price_8:
                                            num_tiers += 1
                                            qty_arr.append(qty_8)
                                            price_arr.append(price_8)

            """
            ************DO UNIQUE NAME******
            """

            s = str(product_name)

            while [s] in name_list:
                tmp = random_permutation('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890',2)
                s = s + ' ' + ''.join(tmp)

            name_list.append([s])
            product_name = s

            """
            ************DO BRANDED*********
            """
            if branded:
                if str(branded.upper()) == "FALSE":
                    branded = 'No'
                elif str(branded.upper()) == "TRUE":
                    branded = 'Yes'

            """
            ***********DO INDENT************
            """
            if indent_only:
                if str(indent_only.upper()) == "FALSE":
                    indent_only = 'No'
                elif str(indent_only.upper()) == "TRUE":
                    indent_only = 'Yes'

            """
            ***********DO COLOUR***********
            """
            #
            single_colour_list = []
            single_colour = str               # BL, BK-NY, RD, GR-WH
            two_code_list = []                  # BK-BK, BK=RD
            colour_list = []                    #
            BE_single_colour = str

            # used for configurable. key is the suppliers colour that is in the image filename.
            # we need to store it now since we convert to BE colour codes
            col_img_dic  = {}


            num_colours = 0     # initialise

            col_img_list = colour_images.split('|')
            len_img_list = len(col_img_list)
            # for img in range(0,len_img_list):


            if colour_cell:
                tmp_col_lst = []
                tmp_col_lst = colour_cell.split("|")      # Black | Blue,Red | Green -> ['Black','Blue,Red','Green']

                idx = 0
                num_colours = len(tmp_col_lst)     # for configurable
                if num_colours > 0:
                    for colour in tmp_col_lst: # check 2-tone
                        # do image matching first
                        bracketed_colour = '(' + colour + ')'     # prevents finding just Black
                        for n in range(0,len_img_list):
                            if bracketed_colour in col_img_list[n]:
                                idx = n

                        # check for two tone colours
                        if ',' in colour:
                            tone_list = colour.split(',')   # ['Charcoal','Light pink']
                            primary = tone_list[0]          # 'Charcoal'
                            secondary = tone_list[1]        # 'Light pink'
                            # first convert supplier colour to BE colour code
                            prim_BE_code = mylib.convert_supp_col_to_BE_code(primary)  # GY
                            sec_BE_code = mylib.convert_supp_col_to_BE_code(secondary) # PK
                            # second convert BE code to a BE colour name
                            prim_BE_colour = mylib.convert_BE_code_to_BE_col(prim_BE_code)      # Gray
                            sec_BE_colour = mylib.convert_BE_code_to_BE_col(sec_BE_code)        # Pink

                            # add to list for
                            single_colour_list.append(constants.BE_CLUT[prim_BE_code])
                            #single_colour_list.append(constants.BE_CLUT[prim_BE_code])

                            two_code_join = prim_BE_code + '-' + sec_BE_code    # GY-PK
                            two_code_list.append(two_code_join) #
                            two_colour_join = str(prim_BE_colour) + '-' + str(sec_BE_colour)    # Gray-Pink
                            colour_list.append(two_colour_join)    #

                            col_img_dic.update({two_colour_join:col_img_list[idx]}) #Gray-Pink: Charcoal,Light pink

                        else:       # single colour only eg. Cool Grey
                            prim_BE_code = mylib.convert_supp_col_to_BE_code(colour)  # GY
                            prim_BE_colour = mylib.convert_BE_code_to_BE_col(prim_BE_code)  # Gray
                            single_colour = constants.BE_CLUT[prim_BE_code]
                            # single_code_list.append(prim_BE_code)
                            two_code_list.append(prim_BE_code)
                            colour_list.append(prim_BE_colour)

                            col_img_dic.update({single_colour: col_img_list[idx]})
                            single_colour_list.append(constants.BE_CLUT[prim_BE_code])

            """
            ******** DO SIZES **********
            """

            size_list = []
            num_sizes = 0   # init


            if product_sizes:
                size_list = product_sizes.split('|')
                num_sizes = len(size_list)

            """
            ********DO CATEGORIES**********
            """

            category_list = []
            num_categories = 0
            category_return = []
            temp_list = []
            if categorisation:  # check cell not empty
                category_list = categorisation.split('|')  # JACKETS|WEATHER/ACTIVEWEAR -> JACKETS , WEATHER/ACTIVEWEAR
                num_categories = len(category_list)  # length = 2

                for level in range(num_categories - 1, -1, -1):  # start from tail of path
                    cat_item = category_list[level]
                    if level == 0:
                        break
                    # if cat_item in category_paths_dic[cat_item]:
                    #         temp_list.append(cat_item)
                    #         break
                    if cat_item == 'NEW':
                        temp_list.append('Default Category/New')
                        # continue
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
                        # break
                        # continue

                    elif cat_item in constants.LEGEND_BE_CATS:  # a few mapped since not in BE
                        temp_list.append(category_paths_dic[constants.LEGEND_BE_CATS[cat_item]])
                        # break
                        # continue
                    elif cat_item in category_paths_dic:
                        temp_list.append(str(category_paths_dic[cat_item]).strip())
                        # break
                        # continue
            category_return = fmt((temp_list))  # #

            """
            ***********DO IMAGE RENAME*************
            """
            #
            # get list of images
            # col_img_list = colour_images.split('|')     #EX3320_colour_image_file(Black).jpg|
            # for col_img in col_img_list:
            #     cols = col_img[col_img.find("(") + 1:col_img.find(")")]     # find string between ()
            #     if ',' in cols:
            #         cols_pair = cols.split(',')
            #         prim = cols_pair[0]
            #         BE_prim = mylib.convert_supplier_col_BEcol(prim)
            #         sec = cols_pair[1]
            #         BE_sec = mylib.convert_supplier_col_BEcol(sec)






            """
            ***********DO GENDER ******************
            """
            #
            # additional_keywords and product name
            # men mens male
            # women womens ladies female
            # kids youth children childrens
            # types: men | women | youth
            gender_return = str
            tmp_str = str
            gender_list = re.findall(r"[\w']+",product_name)
            len_gender_list = len(gender_list)
            if len_gender_list > 0:
                for word in gender_list:
                    if re.match('MEN',word.upper()):
                        tmp_str = 'MEN'
                    elif re.match('WOMEN',word.upper()):
                        tmp_str = 'WOMEN'
                    elif re.match('KID',word.upper()):
                        tmp_str = 'KID'
            else:
                tmp_str = ''

            if isinstance(tmp_str,str):
                gender_return = fmt(tmp_str)
            else:
                gender_return = ""


            """
            ***********DO CLIMATE *****************
            """
            #
            # colder warmer all climate
            # types: cold | warm | all-weather
            # set default to blank since some products will not be a factor!
            climate_return = str
            climate_return = ''

            """
            **********DO MATERIAL *****************
            """
            #
            # work out where materials are displayed and capture
            # if you do nothing just map through
            material_return = str
            material_return = product_materials

            """
            **********DO ECO **********************
            """
            #
            # find eco-friendly products and add category
            # search on 'eco-'

            """
            ***********DO URL-KEY *****************
            """
            url_key_return = str
            url_key_return = url_key_format(product_name)

            """
            ***********DO MARK-UP *****************
            """

            # do by category?
            # set default = 40%
            markup_return = int
            markup_return = 40

            """
            ***********DO CONFIGURABLE*************
            """



            num_ext_rows = 0  # initialise - used for adding rows

            # these do not change during configurable product 20
            set('categories', category_return)
            set('climate', climate_return)
            set('material', material_return)
            set('markup_per', markup_return)
            set('gender', fmt(gender_return))
            set('size', '')
            set('branded',branded)
            set('indent_only',indent_only)
            set('description', product_description)
            #set('description', '')
            set('meta_description','')

            transfer_values(row)  # send values from map

            # create a dataframe
            # get index numbers
            rows = []
            for num in range(0, num_ext_rows + 1):
                rows.append(num)
            # make DataFrame holder
            df_headers = [
                'sku', 'product_type', 'name', 'visibility', 'url_key', 'base_image', 'small_image',
                'thumbnail_image', 'swatch_image', 'color', 'additional_images', 'configurable_variations']

            # create DataFrame object
            df = pd.DataFrame(data=None, index=rows, columns=df_headers)


            """
            SIMPLE TYPE
            """

            # check if configurable and set num extra rows
            if num_colours < 2:   # SIMPLE
                set('sku', product_code)
                set('product_type', 'simple')
                set('name', product_name)
                set('visibility','Catalog, Search')
                set('url_key', url_key_format(url_key_return))
                set('base_image', update_path(base_image,'base'))
                set('small_image',update_path(base_image,'small'))
                set('thumbnail_image',update_path(base_image,'thumb'))
                set('swatch_image','')
                if single_colour_list:
                    set('color', single_colour_list.pop())
                set('additional_images',update_path(additional_images))
                set('configurable_variations','')
                fill_row(dw)                    # finished simple so send to CSV


                if tier_price == True:
                    tier_price = False
                    #for n in range(0,num_tiers):
                    set2('sku',product_code)
                    set2('tier_price_website','All Websites [USD]')
                    set2('tier_price_customer_group','ALL GROUPS')
                    for n in range(0,num_tiers):
                        set2('tier_price_qty',qty_arr[n])
                        set2('tier_price',price_arr[n])
                        dw1.writerow(constants.ADV_PRICING_DIC)


            # CONFIGURABLE TYPE

            else:
                num_ext_rows = num_colours

                # the issue is that the first row depends on the sku and color of configured cells,
                # hence need to store values - DataFrame set up earlier
                cnt = 0
                # row 0
                df.set_value(0, 'sku', product_code)
                df.set_value(0, 'product_type', 'configurable')
                df.set_value(0, 'name', product_name)  # DONE
                df.set_value(0, 'visibility', 'Catalog, Search')  # DONE
                df.set_value(0, 'url_key', url_key_format(product_name))  # DONE
                df.set_value(0, 'base_image', update_path(base_image,'base'))  # DONE
                df.set_value(0, 'small_image', update_path(base_image,'small'))  # DONE
                df.set_value(0, 'thumbnail_image',update_path(base_image,'thumb'))  # DONE
                df.set_value(0, 'swatch_image', '')  # DONE
                df.set_value(0, 'color', '')  # DONE
                df.set_value(0, 'additional_images', update_path(additional_images))  # DONE
                df.set_value(0, 'configurable_variations', '')

                for row in range(1, num_ext_rows + 1):  # plus 1 since the base plus extra
                    tmp_sku = str(product_code) + '-' + str(two_code_list[cnt])

                    df.set_value(row, 'sku', tmp_sku)
                    df.set_value(row, 'product_type', 'simple')
                    df.set_value(row, 'name', str(tmp_sku).lower())  # DONE
                    df.set_value(row, 'visibility', 'Not Visible Individually')  # DONE
                    df.set_value(row, 'url_key', url_key_format(str(tmp_sku).lower()))  # DONE
                    df.set_value(row, 'base_image',update_path(col_img_dic[colour_list[cnt]],'base'))  # DONE
                    df.set_value(row, 'small_image',update_path(col_img_dic[colour_list[cnt]],'small'))  # DONE
                    df.set_value(row, 'thumbnail_image',update_path(col_img_dic[colour_list[cnt]],'thumb'))  # DONE
                    df.set_value(row, 'swatch_image',update_path(col_img_dic[colour_list[cnt]],'swatch'))  # empty on first
                    #df.set_value(row, 'color', constants.BE_CLUT[single_code_list[cnt]])  # DONE
                    df.set_value(row, 'color', single_colour_list[cnt])  # DONE
                    df.set_value(row, 'additional_images', update_path(additional_images))  # DONE
                    df.set_value(row, 'configurable_variations', '')
                    cnt += 1

                # now set up the configuration variations
                config_var = []
                for row in range(1, num_ext_rows + 1):
                    s = str
                    c = str
                    tmp_sku_id = df.at[row, 'sku']
                    tmp_col_id = df.at[row, 'color']
                    config_var.append('sku=' + str(tmp_sku_id) + ',color=' + str(tmp_col_id))
                    if row <= num_ext_rows:      # the last pass
                        config_var.append('|')
                    else:
                        break

                df.set_value(0,'configurable_variations',''.join(config_var))     # can't do this until the end!!

                for i in range(0,len(df)):
                    set('sku',df.iloc[i]['sku'])
                    set('product_type', df.iloc[i]['product_type'])
                    set('name', df.iloc[i]['name'])
                    set('visibility', df.iloc[i]['visibility'])
                    set('url_key', df.iloc[i]['url_key'])
                    set('base_image', df.iloc[i]['base_image'])
                    set('small_image', df.iloc[i]['small_image'])
                    set('thumbnail_image', df.iloc[i]['thumbnail_image'])
                    set('swatch_image', df.iloc[i]['swatch_image'])
                    set('color', df.iloc[i]['color'])
                    set('additional_images', df.iloc[i]['additional_images'])
                    set('configurable_variations', df.iloc[i]['configurable_variations'])
                    fill_row(dw)

                    if tier_price == True:

                        # for n in range(0, num_tiers):
                        set2('sku', df.iloc[i]['sku'])
                        set2('tier_price_website', 'All Websites [USD]')
                        set2('tier_price_customer_group', 'ALL GROUPS')
                        for n in range(0, num_tiers):
                            set2('tier_price_qty', qty_arr[n])
                            set2('tier_price', price_arr[n])
                            dw1.writerow(constants.ADV_PRICING_DIC)

                tier_price = False





            # the following values may need changing so need to be sent through
            product_code = row['product_code']
            product_name = row['product_name']
            categorisation = row['categorisation']
            category__subcategory = row['category__subcategory']
            product_description = row['product_description']
            description_additional = row['description_additional']
            product_features = row['product_features']
            product_materials = row['product_materials']
            base_image = row['product_image_file_name']
            group_image = row['group_image_file_name']
            colour_images = row['colour_image_file_names']
            additional_images = row['alternate_views_image_file_names']
            colour_cell = row['colours_available_supplier']
            product_sizes = row['product_sizes']
            branded = row['branded']
            indent_only = row['indent_only']
            decoration_options_available = row['decoration_options_available']
            decoration_areas = row['decoration_areas']
            price_decoration_description = row['price_decoration_description']
            decoration_type = row['decoration_type']
            additional_keywords = row['additional_keywords']
            qty1 = row['qty_1']
            qty2 = row['qty_2']
            qty3 = row['qty_3']
            qty4 = row['qty_4']
            qty5 = row['qty_5']
            qty6 = row['qty_6']
            qty7 = row['qty_7']
            qty8 = row['qty_8']
            price1 = row['price_1']
            price2 = row['price_2']
            price3 = row['price_3']
            price4 = row['price_4']
            price5 = row['price_5']
            price6 = row['price_6']
            price7 = row['price_7']
            price8 = row['price_8']










