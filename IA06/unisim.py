import sys
import pandas
from pandas import DataFrame

univ_name = sys.argv[1] if len(sys.argv) >=2 else print('Invalid Command, type "-h" for help.')

df = pandas.read_csv('universities.csv', converters={'Expenditures_per_Student': lambda x: int(x.replace('$', '').replace(',',''))})

[df.insert(2*i+3, column + '_STD', (df[column]-df[column].mean())/df[column].std()) for i, column in enumerate(df.iloc[:,2:])]

school_list = list(df['School'])
if univ_name == '-l':
    for name in school_list:
        print (name)
    print ('\n')
    univ_name = input('Type University Name: ')
    if univ_name in school_list:
        pass
    else:
        print ('University not in list. Use "-h" for help.')

if univ_name == '-h':
    print ('This will compute the Euclidean score for the univeristy name provided by the user.')
    print ('It will display the name of university along with the distance closed to the one provided based on the score.')
    print ('')
    print ('For a list of univeristy, use command "-l" to choose from list.')
    print ('The name of university can be directly inputted as command in this format (include quotation): "University Name"')

try:
    if df['School'].str.contains(univ_name).any():
        euclidean = pandas.DataFrame(index=df['School'], columns=['Euclidean'])
        for location, row in df.iterrows():
            euclidean['Euclidean'][location] = ((row['Median_SAT_STD'] - df['Median_SAT_STD']) ** 2 +
                                                (row['Acceptance_Rate_Perc_STD'] - df['Acceptance_Rate_Perc_STD']) ** 2 +
                                                (row['Expenditures_per_Student_STD'] - df['Expenditures_per_Student_STD']) ** 2 +
                                                (row['Graduation_perc_STD'] - df['Graduation_perc_STD']) ** 2)
    #print ('Based on the calculation, a most similar University to {} is {} (Euclidean distance {}), while the least similar is {} (Euclidean distance {})'.format(univ_name))
    print ('Unable to effectively calculate the Euclidean distance ')
except TypeError:
    pass
