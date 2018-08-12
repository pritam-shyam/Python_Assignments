import csv
file = open('second_row.csv', 'w')

with open('sample.csv', 'r') as sample_file:
    reader = csv.reader(sample_file)
    next(reader)
    for row in sample_file.readlines()[::2]:
        file.write(row)
