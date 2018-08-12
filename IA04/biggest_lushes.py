import csv
import time

Iowa_Liquor = open('Iowa_Liquor_Sales.csv')
County_Population = open('County_Population.csv')

Counties_Lush = (open('lush_counties.csv', 'w'))

def function_time(fun):
    def wrap(*args):
        time1 = time.time()
        check = fun(*args)
        time2 = time.time()
        print ('The Function [%s] took %0.2f seconds to complete.' % (fun.__name__, (time2-time1)))
        return check
    return wrap

@function_time
def county_by_volume(inFile):
    reader = csv.reader(inFile)
    next(inFile)
    global unranked
    raw_volume = {}
    dict_list = []
    unranked = {}
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
    rm_list = [[k,round(v,3)] for k,v in raw_volume.items()]
    x = [x for sublist in rm_list for x in sublist]
    unranked = dict(x[i:i+2] for i in range(0, len(x), 2))
    return unranked

@function_time
def county_by_people(inFile2):
    reader = csv.reader(inFile2)
    next(inFile2)
    ranked = {}
    for row in reader:
        county_ranked = []
        county_pop = []
        county_ranked.append(row[0])
        county_pop.append(row[1])
        combo1 = dict(zip(county_ranked, county_pop))
        ranked.update(combo1)
    inFile2.close
    final_list = []
    items = list(unranked.items())
    for k, v in (ranked.items()):
        for i in items:
            if(i[0]) == (k):
              final_list.append([k, i[1], v])

    writer = csv.writer(Counties_Lush)
    writer.writerow(['County Name','Total Volume(Liters)', 'Total Population'])
    for row in list(final_list):
        writer.writerow(row)
    Counties_Lush.close

if __name__ == '__main__':
    start_time = time.time()
    county_by_volume(Iowa_Liquor)
    county_by_people(County_Population)
    minutes = round(((time.time() - start_time)*0.0166667), 2)
    print("Total run time: %s mintues." % minutes)
