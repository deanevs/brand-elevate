import os
import constants


path = constants.RESULTS_PATH
pathout = constants.RESULTS_PATH
in_file = 'Legend Life.csv-2017-01-19 22-47-15.csv'

def split(filehandler, delimiter=',', row_limit=1000,output_name_template= pathout+ 'output_%s.csv', output_path='.',
          keep_headers=True):
    import csv
    reader = csv.reader(filehandler, delimiter=delimiter)
    current_piece = 1
    current_out_path = os.path.join(
        output_path,
        output_name_template % current_piece
    )
    current_out_writer = csv.writer(open(current_out_path, 'w',newline=''), delimiter=delimiter)
    current_limit = row_limit
    if keep_headers:
        headers = next(reader)
        current_out_writer.writerow(headers)
    for i, row in enumerate(reader):
        if i + 1 > current_limit:
            current_piece += 1
            current_limit = row_limit * current_piece
            current_out_path = os.path.join(
                output_path,
                output_name_template % current_piece
            )
            current_out_writer = csv.writer(open(current_out_path, 'w',newline=''), delimiter=delimiter)
            if keep_headers:
                current_out_writer.writerow(headers)
        current_out_writer.writerow(row)







# split(open(path+in_file,'r'))


with open(path+in_file,'r',encoding='utf-8') as fin:
    split(fin)



# csvfile = open(path+in_file,'r',encoding='utf-8').readlines()
#
#
#
# filename = 1
# for i in range(len(csvfile)):
#     if i % 1000 == 0:
#         open(str(filename) + '.csv', 'w+', encoding='utf-8').writelines(csvfile[i:i+1000])
#         filename += 1