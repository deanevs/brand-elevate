# THIS WORKS SO DONT F***
#
# RENAMES ALL THE IMAGE FILES REPLACING ( , )

import os
import re

path = 'C:\\Users\\Dean\\OneDrive\\Business\\Supplier Data\\Legend Life - copy\\Appa File Images'

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


for filename in os.listdir(path):

    new_file = format_filename(filename)
    os.rename(os.path.join(path,filename),os.path.join(path,new_file))





