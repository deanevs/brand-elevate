import pandas as pd
import constants

# Usage: Simply edit the following:
# - supplier name
# - path (if it changes)
# - delimitter type



path = constants.SUPP_PATH
supplier = 'legend life.csv'

df = pd.read_csv(path + supplier)


colset = set()

for cell in df.loc[:,'decoration_options_available']:
    tmp = str(cell).split('|')
    for y in tmp:
        colset.add(y.strip())



for x in colset:
    print (x)
