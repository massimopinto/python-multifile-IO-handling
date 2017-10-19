import csv
import glob

list_of_files = glob.glob('./*.txt') 
for file_name in list_of_files:
  with open(file_name, 'r') as FI, open(file_name.replace('txt', 'out'), 'w') as FO:
    writer = csv.writer(FO, delimiter='\t')
    reader = csv.reader(FI, delimiter='\t')
    NEWcolumns = [5,0,2,3]
    for line in reader:
        newline = [line[i] for i in NEWcolumns]
        newline[2] = newline[2].split('=')[1]
        writer.writerow(newline)
