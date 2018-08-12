import csv
import time
from collections import Counter

Iowa_Liquor = open('Iowa_Liquor_Sales.csv')
Iowa_Liquor1 = open('Iowa_Liquor_Sales.csv')
Iowa_Liquor2 = open('Iowa_Liquor_Sales.csv')
Iowa_Liquor3 = open('Iowa_Liquor_Sales.csv')
Iowa_Liquor4 = open('Iowa_Liquor_Sales.csv')
Iowa_Liquor5 = open('Iowa_Liquor_Sales.csv')

Bottle_Size = (open('bottle_sizes.csv', 'w'))
Top_Products = (open('top_products.csv', 'w'))
Monthly_Rank = (open('monthly.csv', 'w'))
Stores_Ten = (open('stores.csv', 'w'))
Counties_Ten = (open('counties.csv', 'w'))
Cities_Ten = (open('cities.csv', 'w'))

def function_time(fun):
    def wrap(*args):
        time1 = time.time()
        check = fun(*args)
        time2 = time.time()
        print ('The Function [%s] took %0.2f seconds to complete.' % (fun.__name__, (time2-time1)))
        return check
    return wrap

@function_time
def bottle_size(inFile):
    reader = csv.reader(inFile)
    next(inFile)
    bottle_volume = []
    for row in reader:
        bottle_volume.append(row[17])
    inFile.close
    count = Counter()
    for word in bottle_volume:
        count[word] += 1
    total = (Counter(count).most_common(10))
    writer = csv.writer(Bottle_Size)
    writer.writerow(['Bottle Size (ml)', 'Total'])
    writer.writerows(total)
    Bottle_Size.close

@function_time
def top_products(inFile):
    reader = csv.reader(inFile)
    next(inFile)
    product_list = []
    for row in reader:
        product_list.append(row[15])
    inFile.close
    count = Counter()
    for word in product_list:
        count[word] += 1
    total = (Counter(count).most_common(10))
    writer = csv.writer(Top_Products)
    writer.writerow(['Product Name', 'Total'])
    writer.writerows(total)
    Top_Products.close

@function_time
def monthly_rank(inFile):
    reader = csv.reader(inFile)
    next(inFile)
    raw_sales = {}
    dict_list = []
    for row in reader:
        date_list = []
        sales = []
        if row[1][6:] == '2016':
            date_list.append(row[1][:2])
            sales.append(float(row[21][1:]))
            combo = (dict(zip(date_list, sales)))
            dict_list.append(combo)
        else:
            continue
    for item in dict_list:
        for k,v in item.items():
            if k in raw_sales:
                raw_sales[k] += v
            else:
                raw_sales[k] = v
    complete_list = [[k,round(v,3)] for k,v in raw_sales.items()]
    final_list = sorted(complete_list, key=lambda k: k[1], reverse=True)
    writer = csv.writer(Monthly_Rank)
    writer.writerow(['Month', 'Total Sales'])
    writer.writerows(final_list)
    Monthly_Rank.close

@function_time
def ten_stores(inFile):
    reader = csv.reader(inFile)
    next(inFile)
    raw_volume = {}
    dict_list = []
    for row in reader:
        store_list = []
        volume = []
        store_list.append(row[3])
        volume.append(float(row[22]))
        combo = (dict(zip(store_list, volume)))
        dict_list.append(combo)
    inFile.close
    for item in dict_list:
        for k,v in item.items():
            if k in raw_volume:
                raw_volume[k] += v
            else:
                raw_volume[k] = v
    complete_list = [[k,round(v,3)] for k,v in raw_volume.items()]
    final_list = complete_list[:10]
    writer = csv.writer(Stores_Ten)
    writer.writerow(['Store Name', 'Total Volume(Liters)'])
    writer.writerows(final_list)
    Stores_Ten.close

@function_time
def ten_counties(inFile):
    reader = csv.reader(inFile)
    next(inFile)
    raw_volume = {}
    dict_list = []
    for row in reader:
        counties_list = []
        volume = []
        counties_list.append(row[9])
        volume.append(float(row[22]))
        combo = (dict(zip(counties_list, volume)))
        dict_list.append(combo)
    inFile.close
    for item in dict_list:
        for k,v in item.items():
            if k in raw_volume:
                raw_volume[k] += v
            else:
                raw_volume[k] = v
    complete_list = [[k,round(v,3)] for k,v in raw_volume.items()]
    final_list = complete_list[:10]
    writer = csv.writer(Counties_Ten)
    writer.writerow(['County', 'Total Volume(Liters)'])
    writer.writerows(final_list)
    Counties_Ten.close

@function_time
def ten_cities(inFile):
    reader = csv.reader(inFile)
    next(inFile)
    raw_volume = {}
    dict_list = []
    for row in reader:
        city_list = []
        volume = []
        city_list.append(row[5])
        volume.append(float(row[22]))
        combo = (dict(zip(city_list, volume)))
        dict_list.append(combo)
    inFile.close
    for item in dict_list:
        for k,v in item.items():
            if k in raw_volume:
                raw_volume[k] += v
            else:
                raw_volume[k] = v
    complete_list = [[k,round(v,3)] for k,v in raw_volume.items()]
    final_list = complete_list[:10]
    writer = csv.writer(Cities_Ten)
    writer.writerow(['City', 'Total Volume(Liters)'])
    writer.writerows(final_list)
    Cities_Ten.close

if __name__ == '__main__':
    start_time = time.time()
    bottle_size(Iowa_Liquor)
    top_products(Iowa_Liquor1)
    monthly_rank(Iowa_Liquor2)
    ten_stores(Iowa_Liquor3)
    ten_counties(Iowa_Liquor4)
    ten_cities(Iowa_Liquor5)
    minutes = round(((time.time() - start_time)*0.0166667), 2)
    print("Total run time: %s mintues." % minutes)
