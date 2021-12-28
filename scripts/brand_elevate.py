"""
Functions to be commonly used with supplier files
"""



class brand_elevate(object):

    ### Globals
    path = "C:\\Users\\Dean\\OneDrive\\Business\\Supplier Data\\"

    seller_list = ['BIC', 'Biz Collection', 'Bottle of Australia', 'Gloweave', 'Headwear Professionals',
                   'High Caliberline',
                   'JBs wear', 'Legend Life', 'Logoline', 'Nottage', 'ORSO', 'Pen Australia', 'Promo Collection',
                   'Promotional IT Solutions CAPRINA', 'Texet', 'The Source', 'Trends Collection', 'Zen Imports']

####
    def print_sellers_list(lst):
        num = 1
        for x in lst:
            print (str(num) + "." + "\t" + x)
            num += 1
####
#Returns: suppliers name

    def select_path(sel,lst):
        return lst[sel-1]

####
# Returns: full path with end '\' added
    def check_path_end(str):
        if (str[-1] != '\\'):
            str += "\\"
        return str

    ### Program
    print ("Please select supplier:")
    print_sellers_list(seller_list)
    sel =  int(input("User's input: "))



    supplier = select_path(sel,seller_list)
    comp_path = check_path_end(path + supplier)
    print (comp_path)

