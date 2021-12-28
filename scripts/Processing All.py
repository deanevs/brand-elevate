import csv
from BrandElevate_old import mylib
from BrandElevate_old import constants

supplier_name = 'Legend Life'



in_path = constants.SUPP_PATH
out_path = constants.RESULTS_PATH



infile = in_path + supplier_name + ".csv"
outfile = out_path + supplier_name + "-" + mylib.get_datetime() + ".csv"

COLUMNS_ADD = ['sku','name','product_type','ORIG_COL','BE_code','BE_code_tone','BE_colour','BE_size','ORIG_CAT','BE_category']

# Opens supplier file, retrieves its headers and adds BE cols to end
# returns list of headers
def get_infile_headers():
    with open(infile,'r',encoding='utf-8') as fin:
        dr = csv.DictReader(fin, delimiter=',')
        lst = dr.fieldnames
    return (lst)

# *****************************************************
# MAIN PROGRAM
# *****************************************************

extended_headers = get_infile_headers() + COLUMNS_ADD

# construct dictionary for each category and its associated path
dic_BE_cats = mylib.get_BE_cat_paths()


with open(infile,'r',encoding='utf8') as fin:
    dr = csv.DictReader(fin)

    with open(outfile,'w',encoding='utf8',newline='') as fout:
        dw = csv.DictWriter(fout, delimiter=',', fieldnames=COLUMNS_ADD, extrasaction='ignore')
        headers = {}
        for n in dw.fieldnames:
            headers[n] = n
        dw.writerow(headers)

        cnt = 0
        for row in dr:
            # get cells
            colour_cell = row['colours_available_supplier']
            size_cell = row['product_sizes']
            category_cell = row['categorisation']
            product_code_cell = row['product_code']     # unique product code
            product_name_cell = row['product_name']             # name of product



            # variables for calculating configurable
            num_colours = int       # note this needs to be done on the fly since the
            num_sizes = int         # calcs are based per row.  These get reset each time
            num_colours = 0
            num_sizes = 0

            #***********DO COLOUR***********
            BE_code_ret = []             # each gets reinitialised for each row
            BE_code_tone_ret = []
            BE_colour_ret = []

            if colour_cell:
                lst_cell = colour_cell.split("|")       # Black|Blue,Red|Green -> ['Black','Blue,Red','Green']

                num_colours = len(lst_cell)             # for configurable

                for colour in lst_cell: # check 2-tone
                    lst = colour.split(',')             # ['Blue','Red']
                    if len(lst) > 1:
                        #print (lst)
                        prim = lst[0]       # 'Blue'
                        sec = lst[1]           # 'Red'
                        prim_BE_coded = mylib.convert_supp_col_to_BE_code(prim)  # 'BL' or 'MISSING- Blue"
                        sec_BE_coded = mylib.convert_supp_col_to_BE_code(sec)       # 'RD' or '....
                        prim_BE_col = mylib.convert_BE_code_to_BE_col(prim_BE_coded)     #
                        sec_BE_col = mylib.convert_BE_code_to_BE_col(sec_BE_coded)
                        #print (prim_BE_coded)
                        BE_code_ret.append(prim_BE_coded)   # RD
                        a = prim_BE_coded + '-' + sec_BE_coded
                        BE_code_tone_ret.append(a) # BL-RD
                        b = str(prim_BE_col) + '-' + str(sec_BE_col)
                        BE_colour_ret.append(b)    # BLUE-RED

                    else:
                        code2 = mylib.convert_supp_col_to_BE_code(colour)
                        col2 = mylib.convert_BE_code_to_BE_col(code2)

                        BE_code_ret.append(code2)
                        BE_code_tone_ret.append(code2)
                        BE_colour_ret.append(col2)


            # ***********DO SIZES***********
            size_list = []
            size_cell_ret = []
            if size_cell:
                size_list = size_cell.split('|')
                num_sizes = len(size_list)
                for size in range(0,num_sizes):
                    size_cell_ret.append(size_list[size])

            else:
                size_cell_ret = size_cell


            # ********DO CATEGORIES**********

            cats_list = category_cell.split('|')    # JACKETS|WEATHER/ACTIVEWEAR -> JACKETS,WEATHER/ACTIVEWEAR
            len_cats = len(cats_list)               # length = 2
            for level in range(len_cats-1, -1, -1):  # 1 to 0
                cat_ret = cats_list[level]
                if level == 0:
                    #cat_ret = cat_temp
                    break

                if cat_ret in constants.LEGEND_BE_CATS:
                    cat_ret = constants.LEGEND_BE_CATS[cat_ret]
                if  cat_ret in constants.CAT_DOUBLES:
                    # need to go deeper later
                    continue
                if cat_ret in dic_BE_cats:
                    cat_ret = dic_BE_cats[cat_ret]
                    #cat_ret = str(tmp)
                    break


            cat_ret = mylib.fmt(str(cat_ret))   # format it for Magento import

            # ***********DO CONFIGURABLE*************
            sku_start = product_code_cell
            name_start = product_name_cell
            code_tone_list = BE_code_tone_ret
            code_list = BE_code_ret


            # return variables
            sku_ret = str
            product_name_ret = str
            type_ret = str

            # set up types to prevent typos
            type = ['simple','grouped','configurable','virtual','bundle']

            num_ext_rows = 0  # initialise - used for adding rows


            if (num_colours <= 1 and num_sizes <= 1):
                num_ext_rows = 0
                sku_ret = sku_start
                product_name_ret = name_start
                type_ret = 'simple'
                BE_code_ret = ''
                size_cell_ret = ''
                dw.writerow({
                    'sku': sku_ret,
                    'name': product_name_ret,
                    'product_type': type_ret,
                    'BE_code': mylib.fmt(str(BE_code_ret)),
                    'BE_code_tone': mylib.fmt(str(BE_code_tone_ret)),
                    'BE_colour': mylib.fmt(str(BE_colour_ret)),
                    'BE_size': size_cell_ret,
                    #'BE_category': mylib.fmt(str(cat_ret)),
                    'BE_category': cat_ret,
                    'ORIG_CAT': category_cell,
                    'ORIG_COL': colour_cell
                })

            # SIZES ONLY
            elif (num_colours == 0 and num_sizes > 1):
                num_ext_rows = num_sizes
                sku_ret = sku_start
                product_name_ret = product_name_cell
                type_ret = 'configurable'
                BE_code_ret = ''
                #size_cell_ret = ''
                # write first row unchanged but configurable
                dw.writerow({
                    'sku': sku_ret,
                    'name': product_name_ret,
                    'product_type': type_ret,
                    'BE_code': mylib.fmt(str(BE_code_ret)),         # CHANGE to single
                    'BE_code_tone': mylib.fmt(str(BE_code_tone_ret)),
                    'BE_colour': mylib.fmt(str(BE_colour_ret)),
                    'BE_size': mylib.fmt(str(size_cell_ret)),       # CHANGE to single
                    #'BE_category': mylib.fmt(str(cat_ret)),
                    'BE_category': cat_ret,
                    'ORIG_CAT': category_cell,       # pass through
                    'ORIG_COL': colour_cell  # pass through
                })
                for add_row in range(0,num_ext_rows):
                    sku_ret = sku_start     # need to initialise at start
                    #product_name_ret = sku_ret   #not needed
                    type_ret = 'simple'
                    BE_code_ret = ''        # no colours hence empty
                    size_cell_ret = size_list[add_row]
                    sku_ret = sku_start + '-' + str(size_cell_ret)
                    dw.writerow({
                        'sku': sku_ret,
                        'name': sku_ret,    # configurable so the same as sku
                        'product_type': type_ret,
                        'BE_code': mylib.fmt(str(BE_code_ret)),
                        'BE_code_tone': mylib.fmt(str(BE_code_tone_ret)),
                        'BE_colour': mylib.fmt(str(BE_colour_ret)),
                        'BE_size': size_cell_ret,
                        #'BE_category': mylib.fmt(str(cat_ret)),
                        'BE_category': cat_ret,
                        'ORIG_CAT': category_cell,
                        'ORIG_COL': colour_cell
                    })

            # COLOURS ONLY
            elif (num_colours > 1 and num_sizes == 0):
                num_ext_rows = num_colours
                sku_ret = sku_start
                product_name_ret = product_name_cell
                type_ret = 'configurable'
                dw.writerow({
                    'sku': sku_ret,
                    'name': product_name_ret,
                    'product_type': type_ret,
                    'BE_code': mylib.fmt(str(BE_code_ret)),
                    'BE_code_tone': mylib.fmt(str(BE_code_tone_ret)),
                    'BE_colour': mylib.fmt(str(BE_colour_ret)),
                    'BE_size': mylib.fmt(str(size_cell_ret)),
                    #'BE_category': mylib.fmt(str(cat_ret)),
                    'BE_category': cat_ret,
                    'ORIG_CAT': category_cell,
                    'ORIG_COL': colour_cell
                })
                for add_row in range(0,num_ext_rows):
                    sku_ret = sku_start
                    product_name_ret = sku_ret
                    type_ret = 'simple'
                    BE_code_ret = code_list[add_row]
                    sku_ret = sku_start + '-' + str(code_tone_list[add_row])
                    dw.writerow({
                        'sku': sku_ret,
                        'name': sku_ret,
                        'product_type': type_ret,
                        'BE_code': BE_code_ret,
                        'BE_code_tone': mylib.fmt(str(BE_code_tone_ret)),
                        'BE_colour': mylib.fmt(str(BE_colour_ret)),
                        'BE_size': size_cell_ret,
                        #'BE_category': mylib.fmt(str(cat_ret)),
                        'BE_category': cat_ret,
                        'ORIG_CAT': category_cell,
                        'ORIG_COL': colour_cell
                    })
            else:   # both greater than 1
                num_ext_rows = num_colours * num_sizes
                code_list = BE_code_ret
                sku_ret = sku_start
                product_name_ret = product_name_cell
                type_ret = 'configurable'
                dw.writerow({
                    'sku': sku_ret,
                    'name': product_name_ret,
                    'product_type': type_ret,
                    'BE_code': mylib.fmt(str(BE_code_ret)),
                    'BE_code_tone': mylib.fmt(str(BE_code_tone_ret)),
                    'BE_colour': mylib.fmt(str(BE_colour_ret)),
                    'BE_size': mylib.fmt(str(size_cell_ret)),
                    #'BE_category': mylib.fmt(str(cat_ret)),
                    'BE_category': cat_ret,
                    'ORIG_CAT': category_cell,
                    'ORIG_COL': colour_cell
                })
                for add_row in range(0,num_ext_rows):
                    product_name_ret = sku_ret
                    type_ret = 'simple'

                    # calc sku name
                    for col in range(0,len(code_tone_list)):
                        for size in range(0,len(size_list)):
                            sku_ret = sku_start + '-' + str(code_tone_list[col]) + '-' + str(size_list[size])
                            BE_code_ret = code_list[col]
                            size_cell_ret = size_list[size]
                            dw.writerow({
                                'sku': sku_ret,
                                'name': sku_ret,
                                'product_type': type_ret,
                                'BE_code': BE_code_ret,
                                'BE_code_tone': mylib.fmt(str(BE_code_tone_ret)),
                                'BE_colour': mylib.fmt(str(BE_colour_ret)),
                                'BE_size': size_cell_ret,
                                #'BE_category': mylib.fmt(str(cat_ret)),
                                'BE_category': cat_ret,
                                'ORIG_CAT': category_cell,
                                'ORIG_COL': colour_cell
                            })















