import csv
import legend
import constants
import mylib
import re
import pandas as pd

supplier_filename = 'Leg few lines simple product only.csv'

# file IO setup
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
    transfer_values()   # sets values from supplier to import dictionary
    map_eq_fields()     # maps fields that are the same in the import dictionary
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
def transfer_values(dic1=legend.LEGEND_MAP, dic2=constants.MAGENTO_IMPORT_DIC):
    for k in dic1:
        dic2[dic1[k]] = row[k]
    return

# Helper to maps fields in the import file that have the same value.
# e.g. product_name is also the Meta Title
def map_eq_fields(imp=constants.MAGENTO_IMPORT_DIC,map=constants.SET_EQUAL_FIELDS_DIC):
    for key in map:
        imp[key] = imp[map[key]]
    return

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
            col_img_dic  = {}

            num_colours = 0     # initialise

            col_img_list = colour_images.split('|')

            if colour_cell:
                tmp_col_lst = []
                tmp_col_lst = colour_cell.split("|")      # Black | Blue,Red | Green -> ['Black','Blue,Red','Green']

                num_colours = len(tmp_col_lst)     # for configurable
                if num_colours > 0:
                    for colour in tmp_col_lst: # check 2-tone
                        # do image matching first
                        list_index = int    # holds index for matching image
                        bracketed_colour = '(' + colour + ')'     # prevents finding just Black
                        if bracketed_colour in col_img_list:
                            list_index = col_img_list.index(bracketed_colour)


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
                            # used in configurable settings
                            col_img_dic.update({two_colour_join:col_img_list[list_index]})

                        else:       # single colour only
                            prim_BE_code = mylib.convert_supp_col_to_BE_code(colour)
                            prim_BE_colour = mylib.convert_BE_code_to_BE_col(prim_BE_code)

                            single_code_list.append(prim_BE_code)
                            two_code_list.append(prim_BE_code)
                            colour_list.append(prim_BE_colour)


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

            # these do not change during configurable product
            set('categories', category_return)
            set('climate', climate_return)
            set('material', material_return)
            set('markup_per', markup_return)
            set('gender', fmt(gender_return))

            # check if configurable and set num extra rows
            if num_colours > 1 or num_sizes > 1:            # configurable product
                product_type = 'configurable'
                if num_colours > 0 and num_sizes > 0:
                    num_ext_rows = num_colours * num_sizes
                elif num_colours == 0:
                    num_ext_rows = num_sizes
                else:
                    num_ext_rows = num_colours

                # get index numbers
                rows = []
                for num in range(0, num_ext_rows):
                    rows.append(num)

                # make DataFrame holder
                df_headers = ['sku', 'product_type', 'name', 'visibility','url_key', 'base_image', 'small_image',
                              'thumbnail_image', 'swatch_image', 'size', 'color', 'additional_images',
                              'configurable_variations','categories', 'climate', 'material', 'markup_per', 'gender']

                # create DataFrame object
                df = pd.DataFrame(data=None, index=rows, columns=df_headers)


                # fill DataFrame
                for row in range(0,num_ext_rows):
                    if row == 0:
                        df.at[row:'sku'] = product_code
                        df.at[row:'product_type'] = 'configurable'
                        df.at[row:'name'] = product_name
                        df.at[row:'visibility'] = 'Catalog, Search'
                        df.at[row:'url_key'] = url_key_format(product_name)
                        df.at[row:'base_image'] = base_image
                        df.at[row:'small_image'] = base_image
                        df.at[row:'thumbnail_image'] = base_image
                        df.at[row:'swatch_image'] = ''      # empty on first
                        df.at[row:'size'] = ''              # empty on first
                        df.at[row:'color'] = ''             # empty on first
                        df.at[row:'additional_images'] = additional_images
                        df.at[row:'configurable_variations'] = additional_images

                    else:   # now fill all the other rows


                        df.at[row:'sku'] = product_code                             # to do
                        df.at[row:'product_type'] = 'simple'
                        df.at[row:'name'] = str(product_code).lower()
                        df.at[row:'visibility'] = 'Not Visible Individually'
                        df.at[row:'url_key'] = url_key_format(str(product_code).lower())
                        df.at[row:'base_image'] = base_image                        # match the colour image
                        df.at[row:'small_image'] = base_image
                        df.at[row:'thumbnail_image'] = base_image
                        df.at[row:'swatch_image'] = base_image
                        df.at[row:'size'] =                                         # to do
                        df.at[row:'color'] =                                        # to do
                        df.at[row:'additional_images'] = base_image
                        #df.at[row:'configurable_variations'] =                      # can't do this until the end!!

                config_var = str
                for row in range(1,num_ext_rows):
                    config_var = 'sku=' + df.iloc[row:'sku']

                df.at[0:'configurable_variations'] =



                # wrting one row of DataFrame is the equivalent of all the sets below!!
                for row in range(0,num_ext_rows):
                    transfer_values(df.iloc[0])
                    fill_row(dw)


            else:                                           # simple product
                set('sku', product_code)
                set('product_type', 'simple')
                set('description',product_description)
                set('name', product_name)
                set('visibility','Catalog, Search')
                set('url_key', url_key_format(url_key_return))
                set('base_image', base_image)
                set('small_image',base_image)
                set('thumbnail_image',base_image)
                set('swatch_image','')
                set('size',size_list)
                set('color', colour_list)
                set('additional_images',additional_images)
                set('configurable_variations','')

                fill_row(dw)









