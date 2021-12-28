import csv
from BrandElevate_old import mylib
from BrandElevate_old import constants
from BrandElevate_old import Legend

supplier_name = 'Leg few lines'

leg = Legend.LEGEND_MAP
imp = constants.MAGENTO_IMPORT_DIC

in_path = constants.SUPP_PATH
out_path = constants.RESULTS_PATH



infile = in_path + supplier_name + ".csv"
outfile = out_path + supplier_name + "-" + mylib.get_datetime() + ".csv"



# Opens supplier file, retrieves its headers and adds BE cols to end
# returns list of headers
def get_infile_headers():
    with open(infile,'r',encoding='utf-8') as fin:
        dr = csv.DictReader(fin, delimiter=',')
        lst = []
        lst = dr.fieldnames
    return (lst)

# *****************************************************
# MAIN PROGRAM
# *****************************************************
# head = []
# head = get_infile_headers()

# dic1 = import
# dic2 = supplier
def transfer_values(dic1={},dic2={}):
    for k in dic2:
        dic1[dic2[k]] = row[k]
    return

def fill_row(dw,dic):
    dw.writerow(dic)

#dic = {'price_1'}

with open(infile,'r',encoding='utf8') as fin:
    dr = csv.DictReader(fin)
    headers = dr.fieldnames
    with open(outfile,'w',encoding='utf8',newline='') as fout:

        dw = csv.DictWriter(fout, delimiter=',', fieldnames=constants.MAGENTO_HEADERS, extrasaction='ignore')
        dw.writeheader()
        for row in dr:
            transfer_values(imp,leg)
            for k in constants.SET_EQUAL_FIELDS:
                constants.MAGENTO_IMPORT_DIC[k] = constants.MAGENTO_IMPORT_DIC[constants.SET_EQUAL_FIELDS[k]]
            dw.writerow(imp)




