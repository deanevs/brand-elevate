import os
import fnmatch
import constants
import mylib
import csv

supplier_filename = 'Legend Life.csv'
path = 'C:\\Users\\Dean\\OneDrive\\Business\\Supplier Data\\Legend Life'

# file IO setup
test_path = "C:\\Users\\Dean\\Dropbox\\Brand Elevate\\6 Website\\Programming\\Test Files\\"
in_path = constants.SUPP_PATH
out_path = constants.RESULTS_PATH

infile = in_path + supplier_filename
outfile = out_path + supplier_filename + "-" + mylib.get_datetime() + ".csv"




def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


with open(infile,'r',encoding='utf-8') as fin:
    reader = csv.DictReader(fin)
    with open(outfile,'w') as fout:
        writer = csv.writer(fout)


        for row in reader:
            img = row['product_image_file_name']
            alt_views = row['alternate_views_image_file_names']     # list
            col_img = row['colour_image_file_names']    # list


            for img

            #if isinstance(img,list):

            result = find(img,path)
            print (img + "    " + str(result))
            #writer.writerow(img,result)



