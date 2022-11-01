import csv
from multiprocessing.sharedctypes import Value

#function to obtain highest GDP
def get_highest_gdp(data, year):
    max = float(data[0][year])
    for row in data:
        if float(row[year]) > max:
            max = float(row[year])
            highestGDPstate = row["GeoName"]
    return highestGDPstate

#function to obtain lowest GDP
def get_lowest_gdp(data, year):
    min = float(data[0][year])
    for row in data:
        if float(row[year]) < min:
            min = float(row[year])
            lowestGDPstate = row["GeoName"]
    return lowestGDPstate  

#function to obtain GDP of an specific state
def get_state_gdp(data, state, year):
    stateGDP = float(data[0][year])
    for row in data:
        if state == row["GeoName"]:
            stateGDP = float(row[year])
    return stateGDP
   
# save each row into a list 
list_data = []
with open("state_gdp_analysis.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    # go through each year and get gdp values
    for row in reader:
        list_data.append(row)

# get highest gdp for 2020 using "get_highest_gdp(list_data, '2020')"
print(f'Highest GDP is: {get_highest_gdp(list_data,"2020")}')

# get lowest gdp for 2020 using "get_lowest_gdp(list_data, '2020')"
print(f'Lowest GDP is: {get_lowest_gdp(list_data,"2020")}')

# get state gdp for a given year
state = input("Name of state: ")
year = input("Year: ")
print(f'The GDP of {state} in {year} was {get_state_gdp(list_data,state,year)} millions of current dollars.')

# comparing New York in 2019 vs 2020

newYork2019 = get_state_gdp(list_data,"New York","2019")
newYork2020 = get_state_gdp(list_data,"New York","2020")
differenceNY19and20 = newYork2020 - newYork2019
print(differenceNY19and20)