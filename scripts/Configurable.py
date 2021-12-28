"""
Purpose is to analyse supplier data and create an output file in BE format


"""

import pathlib
from BrandElevate_old import mylib

import pandas as pd

desired_width = 140
pd.set_option('display.width', desired_width)

work_dir = pathlib.PureWindowsPath(r"C:\Users\Dean\Dropbox\Brand Elevate\6 Website\7 UTF8 Supplier Data")

print (work_dir.parts)

print ('parent: {}'.format(work_dir.parent))
mylib.print_line()

print ('hierarchy: ')
for up in work_dir.parents:
    print (up)


p2 = pathlib.WindowsPath('.')
for f in p2.iterdir():
    print (f)


#print (list(p.glob('*.*')))





"""
f_index = 0
for i,j in enumerate(filelist):
    if j == "BIZ.csv":
        f_index = i

print (filelist[f_index])

print (mylib.path_leaf(filelist[3]))

for child in p.iterdir():
    print (child)
    df = pd.read_csv(child)
    print(df)

    #print (df.groupby('colours_available_supplier').sum())

    #print (df.dtypes)
    #print (df.columns)
    #print (df.tail(3))
    #print (df.T[0])
    #print (df[0:2])
    #print (df.loc[:,[0,2]])
    #print (df['brand_name'])
    #print (df.iloc[111:113,:])
    #print (df.iloc[:,10:12])
    #df2 = df.copy()
"""

