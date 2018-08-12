import csv
file = open('states.txt', 'w')
iacount = 0
ilcount = 0

with open('sample.csv', 'r') as sample_file:
    reader = csv.reader(sample_file)
    for row in reader:
        if row[6] == 'IA':
            iacount += 1
        elif  row[6] == 'IL':
                ilcount += 1
<<<<<<< HEAD
    file.write('IA Total = ' + str(iacount))
    file.write(' IL Total = ' + str(ilcount))
=======
    file.write('IA Total: '+ str(iacount))
    file.write(' IL Total: '+ str(ilcount))
>>>>>>> 3fca269c8d7eb93fe09d44214da2dd06be579cd0
