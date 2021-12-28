import re
import pandas as pd


# s = "The cat|sat on's the mat"
# new = s.replace(' ','-')
# print (new)
#
#
#
# a = "bags|BAGS|Bags|bag|BAG|Bag|travel|TRAVEL|Travel|satchels|&|totes|SATCHELS|&|TOTES|Satchels|&|Totes|satchels|&|tote|SATCHELS|&|TOTE|Satchels|&|Tote|technology|TECHNOLOGY|Technology|new|NEW|New|ex3238|EX3238|Ex3238|vertical|shoulder|satchel|VERTICAL|SHOULDER|SATCHEL|Vertical|Shoulder|Satchel|specification|heading|SPECIFICATION|HEADING|Specification|Heading|1680d|polyester/210d|nylon|1680D|POLYESTER/210D|NYLON|1680D|Polyester/210D|Nylon|front|zippered|pocket|with|multi-function|organiser|FRONT|ZIPPERED|POCKET|WITH|MULTI-FUNCTION|ORGANISER|Front|Zippered|Pocket|With|Multi-Function|Organiser|zippered|main|compartment|with|padded|rear|pocket|to|store|and|protect|notebooks/ipads|ZIPPERED|MAIN|COMPARTMENT|WITH|PADDED|REAR|POCKET|TO|STORE|AND|PROTECT|NOTEBOOKS/IPADS|Zippered|Main|Compartment|With|Padded|Rear|Pocket|To|Store|And|Protect|Notebooks/Ipads|®|&REG;|&Reg;|and|14|inch|laptops|AND|14|inch|LAPTOPS|And|14|inch|Laptops|back|slip|pocket|BACK|SLIP|POCKET|Back|Slip|Pocket|tough,|adjustable|shoulder|straps|with|padded|shoulder|pad|TOUGH,|ADJUSTABLE|SHOULDER|STRAPS|WITH|PADDED|SHOULDER|PAD|Tough,|Adjustable|Shoulder|Straps|With|Padded|Shoulder|Pad|solid|branded|zip|pulls|SOLID|BRANDED|ZIP|PULLS|Solid|Branded|Zip|Pulls|product|capacity|PRODUCT|CAPACITY|Product|Capacity|11.5 litres|11.5&NBSP;LITRES|11.5&Nbsp;Litres|product|dimensions|PRODUCT|DIMENSIONS|Product|Dimensions|25cm|w|x|33cm h|x|14cm|d|25CM|W|X|33CM&NBSP;H|X|14CM|D|25Cm|W|X|33Cm&Nbsp;H|X|14Cm|D|ex3238|EX3238|Ex3238|vertical|shoulder|satchel|VERTICAL|SHOULDER|SATCHEL|Vertical|Shoulder|Satchel|decoration|options|DECORATION|OPTIONS|Decoration|Options|embroidery|EMBROIDERY|Embroidery|plastisol|PLASTISOL|Plastisol|screen|print|SCREEN|PRINT|Screen|Print|digital|transfer|DIGITAL|TRANSFER|Digital|Transfer|embroidery|areas|EMBROIDERY|AREAS|Embroidery|Areas|front|pocket:|50mm|diameter|FRONT|POCKET:|50MM|DIAMETER|Front|Pocket:|50Mm|Diameter|back|pocket:|125mm|diameter|BACK|POCKET:|125MM|DIAMETER|Back|Pocket:|125Mm|Diameter|print|/ transfer|areas|PRINT|/&NBSP;TRANSFER|AREAS|Print|/&Nbsp;Transfer|Areas|front|pocket:|80mm w|x|130mm|h|FRONT|POCKET:|80MM&NBSP;W|X|130MM|H|Front|Pocket:|80Mm&Nbsp;W|X|130Mm|H|back pocket:|180mm w|x|170mm|h|BACK&NBSP;POCKET:|180MM&NBSP;W|X|170MM|H|Back&Nbsp;Pocket:|180Mm&Nbsp;W|X|170Mm|H|supacolour|areas|SUPACOLOUR|AREAS|Supacolour|Areas|front|pocket:|80mm w|x|130mm|h|FRONT|POCKET:|80MM&NBSP;W|X|130MM|H|Front|Pocket:|80Mm&Nbsp;W|X|130Mm|H|back pocket:|180mm w|x|170mm|h|BACK&NBSP;POCKET:|180MM&NBSP;W|X|170MM|H|Back&Nbsp;Pocket:|180Mm&Nbsp;W|X|170Mm|H|ex3238-bl|EX3238-BL|Ex3238-Bl|ex3238-esp|EX3238-ESP|Ex3238-Esp"
# b = "Exton Vertical Satchel"
#
# c= a+b
#
# d = re.findall(r"[\w']+",c)
# #e = str(d.lower())
# for x in d:
#     print (x.lower())
# print (d)
#
# for f in d:
#     if re.match('Back',f):
#         print (f)

# images = 'J501_colour_image_file(Black,Tan).jpg|J501_colour_image_file(Navy,Navy).jpg|J501_colour_image_file(Navy,Tan).jpg'
# lst = images.split('|')
# len = len(lst)
#
# dic = {}
#
# colour = 'Black,Tan'
# colour_plus = '(' + colour + ')'
#
# for n in range(0,len):
#     if colour_plus in lst[n]:
#         dic.update({colour:lst[n]})
#         print ('yes')
#     else:
#         print ('no')
#
# print (dic)
#

num = []
num_rows = 5
for n in range(0,num_rows):
    num.append(n)

headers = ['A','B','C']

df = pd.DataFrame(index=num,columns=headers)


df.at[0,'A'] = 'hello'

df.at[3,'B'] = 'world'

print (df)

dic = {'A':None,'B':None,'C':None}

print (dic)

dic= df
for k,v in dic.items():
    print (k,v)

#print (dic)

"""
for x in headers:
    df.at[4,x] = 'yeah'

print (df)

print (df.iloc[3])

dic = {}
dic = df.iloc[3]
df.at[:'A'] = 'five'
print ('******')
print (dic)

# for n in range(0,num_rows):
#     print (df.iloc[n])
"""
