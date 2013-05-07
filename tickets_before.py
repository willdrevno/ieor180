'''
Written by Will Drevno for IEOR 180 2013
'''

import csv

#extracting data from CSV of all ticket data
reader = csv.DictReader(open('all_data.csv'))

cust_entries = []
for row in reader:
    cust_entries.append(row)

NA_F12_before = [] #new alumni that bought tickets for 2012 and have bought tickets before
NA_F11_before = [] #new alumni that bought tickets for 2012 and have bought tickets before
NA_F10_before = [] #new alumni that bought tickets for 2012 and have bought tickets before
NA_F09_before = [] #new alumni that bought tickets for 2012 and have bought tickets before
NA_F08_before = [] #new alumni that bought tickets for 2012 and have bought tickets before
for entries in cust_entries:
    #bought in 2012 and have bought a ticket before
    if entries["NA_F12"] == "Yes" and (entries["NA_F07"] == "Yes" or entries["NA_F08"] == "Yes" or entries["NA_F09"] == "Yes" or entries["NA_F10"] == "Yes" or entries["NA_F11"] == "Yes"):
        NA_F12_before.append(entries)
     #bought in 2011 and have bought a ticket before
    if entries["NA_F11"] == "Yes" and (entries["NA_F07"] == "Yes" or entries["NA_F08"] == "Yes" or entries["NA_F09"] == "Yes" or entries["NA_F10"] == "Yes"):
        NA_F11_before.append(entries)
    #bought in 2010 and have bought a ticket before
    if entries["NA_F10"] == "Yes" and (entries["NA_F07"] == "Yes" or entries["NA_F08"] == "Yes" or entries["NA_F09"] == "Yes"):
        NA_F10_before.append(entries)
    #bought in 2009 and have bought a ticket before
    if entries["NA_F09"] == "Yes" and (entries["NA_F07"] == "Yes" or entries["NA_F08"] == "Yes"):
        NA_F09_before.append(entries)
    #bought in 2008 and have bought a ticket before
    if entries["NA_F08"] == "Yes" and (entries["NA_F07"] == "Yes"):
        NA_F08_before.append(entries)
    

print "bought before, starting in F12"
print len(NA_F12_before)
print len(NA_F11_before)
print len(NA_F10_before)
print len(NA_F09_before)
print len(NA_F08_before)
