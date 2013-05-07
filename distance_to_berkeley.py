'''
Written by Will Drevno for IEOR 180 2013
'''
from latlong import *
import csv

#extracting data from CSV of all ticket data
reader = csv.DictReader(open('all_data.csv'))

cust_entries = []
for row in reader:
    cust_entries.append(row)
    
#extracting data from library of area codes mapped to cities and states
reader = csv.DictReader(open('areacodes.csv'))

area_entries = []
for row in reader:
    area_entries.append(row)
    
#takes in ticket sale data, filters, and then sees which cities phone area codes match up with a particular city
customer_city = []
for business_number in cust_entries:
    if business_number["NA_F13"] == "Yes" or business_number["NA_F12"] == "Yes" or business_number["NA_F11"] == "Yes" or business_number["NA_F10"] == "Yes" or business_number["NA_F09"] == "Yes" or business_number["NA_F08"] == "Yes" or business_number["NA_F07"] == "Yes":
        for areacode in area_entries:
            if business_number["_BusinessPhone_"][1:4] == areacode["Area Code"]:
                customer_city.append(areacode["City"])

#sorting data based on population in each city
quantity_city = [(x, customer_city.count(x)) for x in set(customer_city)]
sorted_data = sorted(quantity_city, key=lambda student: student[1], reverse=True)

#extracting lat-long data
reader = csv.DictReader(open('latlongdata.csv'))

cities_latlong = []
for row in reader:
    cities_latlong.append(row)

#berkeley_latlong data
berkeley_lat = 37.8717
berkeley_long = -122.2859

city_data = [] 
#meant to see if city is within certain distance (within 10 miles, 10-30 miles, 30-50 miles, +50 miles) of Berkeley
for cities in sorted_data:
    for latlong in cities_latlong: #matches city to lat long coordinates
        if cities[0] == latlong["city"]:
            #calculating distance between two points
            distancetocity = distance([float(latlong["latitude"]),float(latlong["longitude"])],[berkeley_lat,berkeley_long])
            if distancetocity < 50 and distancetocity > 30: #filtering based on distance
                dist = distance([float(latlong["latitude"]),float(latlong["longitude"])],[berkeley_lat,berkeley_long])
                city_data.append((cities[0],cities[1]))
                #city_data.append(cities[0])

city_data = list(set(city_data)) #removeing duplicates
print city_data


#less then 10 miles
#10-30
#30-50
#more then 50

    