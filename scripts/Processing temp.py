import csv
from BrandElevate_old import mylib
from BrandElevate_old import constants

supplier_name = 'test'



in_path = constants.SUPP_PATH
out_path = constants.RESULTS_PATH



infile = in_path + supplier_name + ".csv"
outfile = out_path + supplier_name + "-" + mylib.get_datetime() + ".csv"


def get_infile_headers():
    with open(infile,'r',encoding='utf-8') as fin:
        dr = csv.DictReader(fin, delimiter=',')
        lst = dr.fieldnames
    return (lst)

def fill_row(dw_obj,dic):

    dw.writerow(dic)


# *****************************************************
# MAIN PROGRAM
# *****************************************************

supplier_headers = get_infile_headers()


with open(infile,'r',encoding='utf8') as fin:
    dr = csv.DictReader(fin)

    with open(outfile,'w',encoding='utf8',newline='') as fout:
        dw = csv.DictWriter(fout, delimiter=',', fieldnames=supplier_headers, extrasaction='ignore')
        headers = {}
        for n in dw.fieldnames:
            headers[n] = n
        dw.writerow(headers)
        var1 = 'hello'
        var2 = 'world'
        var3 = '!'

        dic = ({'col1':var1,'col2':var2,'col3':var3})

        dic['col1'] = 'changed'
        for row in dr:

            fill_row(dw,dic)







