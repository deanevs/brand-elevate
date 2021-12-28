import csv
from BrandElevate_old import mylib
from BrandElevate_old import constants


infile = "Legend Life.csv"
outfile = "out-" + mylib.get_datetime() + ".csv"

d = {}

# Opens supplier file, retrieves its headers and adds BE cols to end
# returns list of headers
def get_BE_headers():
    with open(infile,'r',encoding='utf-8') as fin:
        dr = csv.DictReader(fin, delimiter=',')
        lst = dr.fieldnames
        cols_add = ['sku','BE_code','BE_col','BE_prim_sec_col''BE_size','BE_category']
        # for fieldname in lst:
        #     d[fieldname] = fieldname        #
    return (lst + cols_add)

# *****************************************************
# MAIN PROGRAM
# *****************************************************

extended_headers = get_BE_headers()

# construct dictionary for each category and its associated path
dic_BE_cats = mylib.get_BE_cat_paths()


with open(infile,'r',encoding='utf8') as fin:
    dr = csv.DictReader(fin)

    with open(outfile,'w',encoding='utf8',newline='') as fout:
        dw = csv.DictWriter(fout, delimiter=',', fieldnames=extended_headers, extrasaction='ignore')
        headers = {}
        for n in dw.fieldnames:
            headers[n] = n
        dw.writerow(headers)
        for row in dr:
            # get cells
            colour_cell = row['colours_available_supplier']
            size_cell = row['product_sizes']
            category_cell = row['categorisation']
            product_code_cell = row['product_code']     # sku

            # variables for calculating configurable
            num_colours = int
            num_sizes = int

            #***********DO COLOUR
            BE_col_ret = []
            BE_prim_sec_col_ret = []
            BE_code_ret = []

            lst_cell = colour_cell.split("|")       # Black|Blue,Red|Green -> ['Black','Blue,Red','Green']
            list_single = []
            list_tone = []
            for colour in lst_cell: # check 2-tone
                lst_prim = colour.split(',')            # ['Blue','Red']
                if len(lst_prim) > 0:
                    primary = lst_prim[0]

                    sec = lst_prim[1]

                    list_tone.append(lst_prim[0] + '-' + lst_prim[1])   # 'Blue-Red'
                    list_single.append(lst_prim[0])
                else:
                    list_tone.append(colour)
                    list_single.append(colour)

            for colour in list_tone:
                if colour in constants.LEG_to_BE:
                    BE_code_ret.append(constants.LEG_to_BE[colour])
                else:
                    BE_code_ret.append('MISSING-' + colour)

            for colour in list_single:
                if colour in constants.LEG_to_BE:
                    BE_code_ret.append(constants.LEG_to_BE[colour])
                else:
                    BE_code_ret.append('MISSING-' + colour)

            for colour in BE_code_ret:
                if colour in constants.BE_CLUT:
                    BE_col_ret.append(constants.BE_CLUT[colour])
                else:
                    BE_col_ret.append("MISSING-" + colour)
            #print (lst_BE_colours)

            # DO CATEGORIES
            cat_return = str
            cat_temp = str
            lst_cats = category_cell.split('|')
            lst_len = len(lst_cats)
            for x in range(lst_len-1,0,-1):

                cat_temp = lst_cats[x]
                if x == 0:
                    cat_return = cat_temp
                    break

                print ('First' +cat_temp)
                if cat_temp in constants.LEGEND_BE_CATS:
                    cat_temp = constants.LEGEND_BE_CATS[cat_temp]
                    print ('Second ' + cat_temp)
                #if  cat_temp in constants.CAT_DOUBLES:
                    # need to go deeper later
                #    continue
                if cat_temp in dic_BE_cats:
                    print ('Third ' + cat_temp)
                    tmp = dic_BE_cats[cat_temp]
                    print (str(tmp))
                    cat_return = str(tmp)
                    #print ('Return '+ cat_return)
                    #tmp = dic_BE_cats[cat_temp]
                    # if len(tmp) > 0:
                    #     cat_return = tmp.pop()
                    #     #print (cat_return)
                    # else:
                    #     cat_return = tmp
                    break
                else:
                    continue

            #print (cat_return)
            dw.writerow({
                'sku': product_code_cell,
                #'colours_available_supplier':colour_cell,
                'BE_code': BE_code_ret,
                'BE_col': BE_col_ret,
                'BE_prim_sec_col':
                'BE_size': size_cell,
                'BE_category': cat_return,
                #'categorisation':category_cell
            })







