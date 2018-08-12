import pandas

df = pandas.read_csv('universities.csv')
df['Expenditures_per_Student'] = df['Expenditures_per_Student'].str.replace('$','')
df['Expenditures_per_Student'] = df['Expenditures_per_Student'].str.replace(',','')
df['Expenditures_per_Student'] = df['Expenditures_per_Student'].astype(int)

columns = list(df.columns)
columns.remove('School')
columns.remove('Type')
df[columns]

for column in columns:
    score = column + ' (Z-Score)'
    df[score] = round((df[column] - df[column].mean())/df[column].std(ddof=0),3)

df['Expenditures_per_Student'] = df['Expenditures_per_Student'].map('${:,.0f}'.format)
df['Expenditures_per_Student (Z-Score)'] = df['Expenditures_per_Student (Z-Score)'].map('${:,.2f}'.format)

df.to_csv('normalized.csv')
