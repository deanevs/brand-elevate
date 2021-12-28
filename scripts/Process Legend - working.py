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

supplier_filename = 'legend 30 products.csv'

# file IO setup
test_path = "C:\\Users\\Dean\\Dropbox\\Brand Elevate\\6 Website\\Programming\\Test Files\\"
in_path = constants.SUPP_PATH
out_path = constants.RESULTS_PATH

infile = test_path + supplier_filename
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
def fmt(lst):
    ch_remove = str.maketrans("", "", "[']{} ")
    tmp = lst.translate(ch_remove)
    if ',' in lst:
        tmp = tmp.replace(',', '|')
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

# *****************************************************
# MAIN PROGRAM
# *****************************************************

# setup dictionaries
category_paths_dic = mylib.get_BE_category_paths()

supplier_headers = get_infile_headers()





with open(infile,'r',encoding='utf8') as fin:
    dr = csv.DictReader(fin)

    with open(outfile,'w',encoding='utf8',newline='') as fout:
        dw = csv.DictWriter(fout, delimiter=',', fieldnames=constants.MAGENTO_HEADERS, extrasaction='ignore')
        #dw.writerow(constants.MAGENTO_HEADERS)
        dw.writeheader()

        for row in dr:
            # map through all values that do not change
            for k in legend.LEGEND_MAP:
                constants.MAGENTO_IMPORT_DIC[legend.LEGEND_MAP[k]] = row[k]

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
            alt_views_images = row['alternate_views_image_file_names']
            group_image = row['group_image_file_name']
            colour_images = row['colour_image_file_names']
            additional_images = row['alternate_views_image_file_names']
            colour_cell = row['colours_available_supplier']
            product_sizes = row['product_sizes']
            decoration_options_available = row['decoration_options_available']
            decoration_areas = row['decoration_areas']
            price_decoration_description = row['price_decoration_description']
            decoration_type = row['decoration_type']
            additional_keywords = row['additional_keywords']





            # ***********DO COLOUR***********

            single_code_list = []               # BL, BK-NY, RD, GR-WH
            two_code_list = []                  # BK-BK, BK=RD
            colour_list = []                    #

            # used for configurable
            col_img_dic  = {}

            num_colours = 0     # initialise

            col_img_list = colour_images.split('|')
            len_img_list = len(col_img_list)

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


                        if ',' in colour:   # check for two tone colours
                            tone_list = colour.split(',')  # ['Blue','Red']
                            primary = tone_list[0]       # 'Blue'
                            secondary = tone_list[1]           # 'Red'
                            prim_BE_code = mylib.convert_supp_col_to_BE_code(primary)  # 'BL' or 'MISSING- Blue"
                            sec_BE_code = mylib.convert_supp_col_to_BE_code(secondary)       # 'RD' or '....
                            prim_BE_colour = mylib.convert_BE_code_to_BE_col(prim_BE_code)     #
                            sec_BE_colour = mylib.convert_BE_code_to_BE_col(sec_BE_code)
                            single_code_list.append(prim_BE_code)   # RD
                            two_code_join = prim_BE_code + '-' + sec_BE_code
                            two_code_list.append(two_code_join) # BL-RD
                            two_colour_join = str(prim_BE_colour) + '-' + str(sec_BE_colour)
                            colour_list.append(two_colour_join)    # BLUE-RED

                            col_img_dic.update({two_colour_join:col_img_list[idx]})

                        else:       # single colour only
                            prim_BE_code = mylib.convert_supp_col_to_BE_code(colour)
                            prim_BE_colour = mylib.convert_BE_code_to_BE_col(prim_BE_code)
                            single_code_list.append(prim_BE_code)
                            two_code_list.append(prim_BE_code)
                            colour_list.append(prim_BE_colour)

                            col_img_dic.update({prim_BE_colour: col_img_list[idx]})


            # print_dic(col_img_dic)


            # print('******supp list******************')
            # print (tmp_col_lst)
            # print('******colour list******************')
            # print(colour_list)
            # print ('*******single code*****************')
            # print (single_code_list)
            # print('********two code****************')
            # print (two_code_list)
            # print ('\n')
            #
            # ***********DO SIZES***********

            size_list = []
            num_sizes = 0   # init


            if product_sizes:
                size_list = product_sizes.split('|')
                num_sizes = len(size_list)


            # ********DO CATEGORIES**********

            category_list = []
            num_categories = 0
            category_return = []
            temp_list = []
            if categorisation:
                category_list = categorisation.split('|')    # JACKETS|WEATHER/ACTIVEWEAR -> JACKETS,WEATHER/ACTIVEWEAR
                num_categories = len(category_list)         # length = 2

                for level in range(num_categories -1, -1, -1):  # start from tail of path
                    cat_item = category_list[level]
                    if level == 0 and cat_item in category_paths_dic[cat_item]:
                        temp_list.append(cat_item)
                        break
                    if cat_item in constants.CAT_DOUBLES:
                        continue    # need to go deeper later
                    elif cat_item in constants.LEGEND_BE_CATS:       # a few mapped since not in BE
                        temp_list.append(category_paths_dic[constants.LEGEND_BE_CATS[cat_item]])
                        break
                    elif cat_item in category_paths_dic:
                        temp_list.append(category_paths_dic[cat_item])
                        break
            category_return = fmt(str(temp_list))   #

            # ***********DO COLOUR IMAGE*************
            # get list of images
            col_img_list = colour_images.split('|')     #EX3320_colour_image_file(Black).jpg|
            for col_img in col_img_list:
                cols = col_img[col_img.find("(") + 1:col_img.find(")")]     # find string between ()
                if ',' in cols:
                    cols_pair = cols.split(',')
                    prim = cols_pair[0]
                    BE_prim = mylib.convert_supplier_col_BEcol(prim)
                    sec = cols_pair[1]
                    BE_sec = mylib.convert_supplier_col_BEcol(sec)







            # ***********DO GENDER ******************
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

            # ***********DO CLIMATE *****************
            # colder warmer all climate
            # types: cold | warm | all-weather
            # set default to blank since some products will not be a factor!
            climate_return = str
            climate_return = ''

            # **********DO MATERIAL *****************
            # work out where materials are displayed and capture
            # if you do nothing just map through
            material_return = str
            material_return = product_materials


            # **********DO ECO **********************
            # find eco-friendly products and add category
            # search on 'eco-'




            # ***********DO URL-KEY *****************
            url_key_return = str
            url_key_return = url_key_format(product_name)




            # ***********DO MARK-UP *****************
            # do by category?
            # set default = 40%
            markup_return = int
            markup_return = 40


            # ***********DO CONFIGURABLE*************

            num_ext_rows = 0  # initialise - used for adding rows

            # these do not change during configurable product 20
            set('categories', category_return)
            set('climate', climate_return)
            set('material', material_return)
            set('markup_per', markup_return)
            set('gender', fmt(gender_return))
            set('size', product_sizes)
            set('description', product_description)
            set('meta_description',product_description)

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

            # check if configurable and set num extra rows
            if num_colours < 2:   # SIMPLE
                set('sku', product_code)
                set('product_type', 'simple')
                set('name', product_name)
                set('visibility','Catalog, Search')
                set('url_key', url_key_format(url_key_return))
                set('base_image', base_image)
                set('small_image',base_image)
                set('thumbnail_image',base_image)
                set('swatch_image','')
                set('color', colour_list)
                set('additional_images',additional_images)
                set('configurable_variations','')


                fill_row(dw)                    # finished simple so send to CSV

            else:   # CONFIGURABLE
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
                df.set_value(0, 'base_image', base_image)  # DONE
                df.set_value(0, 'small_image', base_image)  # DONE
                df.set_value(0, 'thumbnail_image', base_image)  # DONE
                df.set_value(0, 'swatch_image', '')  # DONE
                df.set_value(0, 'color', '')  # DONE
                df.set_value(0, 'additional_images', additional_images)  # DONE
                df.set_value(0, 'configurable_variations', '')

                for row in range(1, num_ext_rows + 1):  # plus 1 since the base plus extra
                    tmp_sku = product_code + '-' + two_code_list[cnt]

                    df.set_value(row, 'sku', tmp_sku)
                    df.set_value(row, 'product_type', 'simple')
                    df.set_value(row, 'name', str(tmp_sku).lower())  # DONE
                    df.set_value(row, 'visibility', 'Not Visible Individually')  # DONE
                    df.set_value(row, 'url_key', url_key_format(str(tmp_sku).lower()))  # DONE
                    df.set_value(row, 'base_image', col_img_dic[colour_list[cnt]])  # DONE
                    df.set_value(row, 'small_image', col_img_dic[colour_list[cnt]])  # DONE
                    df.set_value(row, 'thumbnail_image', col_img_dic[colour_list[cnt]])  # DONE
                    df.set_value(row, 'swatch_image', col_img_dic[colour_list[cnt]])  # empty on first
                    df.set_value(row, 'color', constants.BE_CLUT[single_code_list[cnt]])  # DONE
                    df.set_value(row, 'additional_images', col_img_dic[colour_list[cnt]])  # DONE
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

                # print (''.join(config_var))
                df.set_value(0,'configurable_variations',''.join(config_var))     # can't do this until the end!!

                # print (df)
                # for each row send
                # dic = {'sku': 'somename'}
                # for row in df.itertuples():
                #     dw.writerow(row)
                #     print(row)
                #     break

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





                # dic = {}
                # dic = df.to_dict(orient='dict')
                # print (dic)
                # for items in dic.items():
                #     dw.writerow(items)
                #
                # dw.writerow(dic)




                #wrting one row of DataFrame is the equivalent of all the sets below!!













