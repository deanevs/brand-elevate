import pandas as pd
from collections import defaultdict
import constants



# In Legend Life the categories have the main category first in the list
# Using a dictionary, the key is the first value and the remaining are a set

infile = 'The Range - The Range.csv'
path = constants.SUPP_PATH
outpath = constants.RESULTS_PATH

df = pd.read_csv(path + infile)


fd = open(outpath + "result.txt",'w')

cat_dict = defaultdict(set)

for cell in df.loc[:, 'category_ /_sub category']:
    temp = cell.split('|')
    k = temp.pop(0)
    for x in temp:
        print (x)
        if k not in cat_dict:
            cat_dict[k]=set()
        cat_dict[k].add(x)


for k,v in cat_dict.items():
    fd.write(k + str(v) + '\n')
    print (k,v)

fd.close()
