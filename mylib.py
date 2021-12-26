import datetime
import csv
import constants
import os
import legend


# All files for Brand Elevate project should reside in here
ref_path = constants.REF_PATH



# DATA OPERATIONS

def convert_supp_col_to_BE_code(col):
    code_ret = str
    if col in legend.LEG_to_BE:
        code_ret = legend.LEG_to_BE[col]
    else:
        print ('MISSING-' + str(col))
    return code_ret

def convert_BE_code_to_BE_col(code):
    col_ret = str
    if code in constants.BE_CLUT:
        col_ret = constants.BE_CLUT[code]
    else:
        print ("MISSING-" + str(code))
    return col_ret


# Helper function to convert supplier colour to BE colour
# Black opal -> BK ->black
def convert_supplier_col_BEcol(col):
     return constants.BE_CLUT[constants.LEG_to_BE[col]]


# this works!!!  DON'T MESS
# returns a dictionary with every category being a key with a set of its associated paths
def get_BE_category_paths():

    import csv
    import constants

    ref_path = constants.REF_PATH

    with open(ref_path + "BE Category Full Path.csv",'r') as fd:
        reader = csv.reader(fd)
        category_dic = {}

        for row in reader:
            ch = set('/')
            k = str
            for cell in row:
                path = 'Default Category'
                if ch & set(cell):  # not root
                    lst = cell.split('/')
                    lst_len = len(lst)
                    first = True
                    for x in range(0, lst_len):
                        path = 'Default Category'
                        if first == True:
                            first = False
                        else:
                            k = lst[x].strip()
                            i = 0
                            while i <= x:
                                path = path + '/' + lst[i].strip()
                                i += 1
                else:               # this is the root
                    k = cell.strip()
                    path = path + '/' + k
                    #path = k
                if k not in category_dic:
                    category_dic[k] = set()
                    category_dic[k].add(path)
                else:
                    category_dic[k].add(path)
        return category_dic

dic = get_BE_category_paths()
for k,v in dic.items():
    print (k,v)

# def get_categories(reader=csv.reader):
#     rd = reader
#     dic = {}
#     for row in rd:
#         ch = set('/')
#         k = str
#         for cell in row:
#             path = 'Default Category'
#             if ch & set(cell):  # not root
#                 lst = cell.split('/')
#                 lst_len = len(lst)
#                 first = True
#                 for x in range(0, lst_len):
#                     path = 'Default Category'
#                     if first == True:
#                         first = False
#                     else:
#                         k = lst[x].strip()
#                         i = 0
#                         while i <= x:
#                             path = path + '/' + lst[i].strip()
#                             i += 1
#             else:  # this is the root
#                 k = cell.strip()
#                 path = path + '/' + k
#             if k not in dic:
#                 dic[k] = set()
#                 dic[k].add(path)
#             else:
#                 dic[k].add(path)
#     return dic



# DATETIME OPERATIONS

# Useful for unique filename outs when testing
# Arguments = Nothing
# Returns output 2017-01-09 09:35:15
def get_datetime():
    curr_datetime = datetime.datetime.now()
    newtime = curr_datetime.strftime("%Y-%m-%d %H-%M-%S")
    return newtime



# DEBUGGING TOOLS


# Prints a line of chars to separate debugging output
# Argument = string Default character = *
# Returns = Nothing
def print_line(chr='*'):
    a = chr
    num_chars = 40
    for x in range(0,num_chars):
        print (a,end="")
        if x == num_chars-1:
            print ('\n')
    return



# FILE OPERATIONS

#
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)



# iterate over files in a single directory
import os
for fn in os.listdir('.'):
    if os.path.isfile(fn):
        print(fn)




def split(filehandler, delimiter=',', row_limit=10000, output_name_template='output_%s.csv',
          output_path='.', keep_headers=True):
    """
    Splits a CSV file into multiple pieces.

    A quick bastardization of the Python CSV library.
    Arguments:
        `row_limit`: The number of rows you want in each output file. 10,000 by default.
        `output_name_template`: A %s-style template for the numbered output files.
        `output_path`: Where to stick the output files.
        `keep_headers`: Whether or not to print the headers in each output file.
    Example usage:

        >> from toolbox import csv_splitter;
        >> csv_splitter.split(open('/home/ben/input.csv', 'r'));

    """
    reader = csv.reader(filehandler, delimiter=delimiter)
    current_piece = 1
    current_out_path = os.path.join(output_path,output_name_template % current_piece)
    current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
    current_limit = row_limit
    if keep_headers:
        headers = reader.next()
        current_out_writer.writerow(headers)
    for i, row in enumerate(reader):
        if i + 1 > current_limit:
            current_piece += 1
            current_limit = row_limit * current_piece
            current_out_path = os.path.join(
                output_path,
                output_name_template % current_piece
            )
            current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
            if keep_headers:
                current_out_writer.writerow(headers)

            current_out_writer.writerow(row)