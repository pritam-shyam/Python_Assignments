import csv
file = open('selected_cols.csv', 'w')

with open('sample.csv', 'r') as sample_file:
    reader = csv.reader(sample_file)
    next(reader)
    for row in sample_file.readlines():
        columns = row.split(',')
        first_column = columns[0]
        second_column = columns[1]
        last_column = columns[12-1]
        file.writelines([first_column, second_column, last_column])
