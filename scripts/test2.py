import pandas as pd

def p():
    print ('**********************')

num = []
num_rows = 5
for n in range(0,num_rows):
    num.append(n)

headers = ['A','B','C']

df = pd.DataFrame(index=num,columns=headers)
print (df)
p()
df.at[0,'A'] = 'hello'
#print (df)
df.at[3,'B'] = 'world'
#print (df)
df.at[4,'C'] = 'fuck'

print (df)

for row,index in df.iterrows():
    print (row,index)
    p()


# dic = {}
#
# dic.update({df.iloc[2]})
