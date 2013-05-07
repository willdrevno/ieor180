'''
Written by Will Drevno for IEOR 180 2013
'''

import csv

#extracting data from CSV of all ticket data
reader = csv.DictReader(open('all_data.csv'))

cust_entries = []
for row in reader:
    cust_entries.append(row)

NA_F12 = [] #new alumni that bought football tickets in 2012
NA_F11 = [] #new alumni that bought football tickets in 2011
NA_F10 = [] #etc.
NA_F09 = []
NA_F08 = []
NA_F07 = []
inarow6 = [] #starting in 2012, new alumni that bought 6 times in a row
inarow5 = [] #starting in 2012, new alumni that bought 5 times in a row
inarow4 = [] #etc.
inarow3 = []
inarow2 = []
for entries in cust_entries:
    if entries["NA_F12"] == "Yes": #filter for new alumni tickets sold in 2012
        NA_F12.append(entries)
    if entries["NA_F11"] == "Yes": #filter for new alumni tickets sold in 2011
        NA_F11.append(entries)
    if entries["NA_F10"] == "Yes": #etc.
        NA_F10.append(entries)
    if entries["NA_F09"] == "Yes":
        NA_F09.append(entries)
    if entries["NA_F08"] == "Yes":
        NA_F08.append(entries)
    if entries["NA_F07"] == "Yes":
        NA_F07.append(entries)
    #6 years in a row
    if entries["NA_F07"] == "Yes" and entries["NA_F08"] == "Yes" and entries["NA_F09"] == "Yes" and entries["NA_F10"] == "Yes" and entries["NA_F11"] == "Yes" and entries["NA_F12"] == "Yes":
        inarow6.append(entries)
    #5 years in a row
    if entries["NA_F08"] == "Yes" and entries["NA_F09"] == "Yes" and entries["NA_F10"] == "Yes" and entries["NA_F11"] == "Yes" and entries["NA_F12"] == "Yes":
        inarow5.append(entries)
    if entries["NA_F09"] == "Yes" and entries["NA_F10"] == "Yes" and entries["NA_F11"] == "Yes" and entries["NA_F12"] == "Yes":
        inarow4.append(entries)
    if entries["NA_F10"] == "Yes" and entries["NA_F11"] == "Yes" and entries["NA_F12"] == "Yes":
        inarow3.append(entries)
    if entries["NA_F11"] == "Yes" and entries["NA_F12"] == "Yes":
        inarow2.append(entries)
    
print "Amount of tickets by year starting in 2012"
print len(NA_F12)
print len(NA_F11)
print len(NA_F10)
print len(NA_F09)
print len(NA_F08)
print len(NA_F07)
print "Amount in a row starting at 6"
print len(inarow6)
print len(inarow5)
print len(inarow4)
print len(inarow3)
print len(inarow2)

