'''
Written by Will Drevno for IEOR 180, 2013
'''

import csv

#extracting data from CSV of all ticket data
reader = csv.DictReader(open('all_data.csv'))

cust_entries = []
for row in reader:
    cust_entries.append(row)

F12 = [] #students that bought football tickets in 2012
F11 = [] #students that bought football tickets in 2011
F10 = [] #etc.
F09 = []
F08 = []
F07 = []
inarow6 = [] #starting in 2012, students that bought 6 times in a row
inarow5 = [] #starting in 2012, students that bought 5 times in a row
inarow4 = [] #etc.
inarow3 = []
inarow2 = []
for entries in cust_entries:
    if entries["F12"] == "Yes": #filter for student tickets sold in 2012
        F12.append(entries)
    if entries["F11"] == "Yes": #filter for student tickets sold in 2011
        F11.append(entries)
    if entries["F10"] == "Yes": #etc.
        F10.append(entries)
    if entries["F09"] == "Yes":
        F09.append(entries)
    if entries["F08"] == "Yes":
        F08.append(entries)
    if entries["F07"] == "Yes":
        F07.append(entries)
    #6 years in a row
    if entries["F07"] == "Yes" and entries["F08"] == "Yes" and entries["F09"] == "Yes" and entries["F10"] == "Yes" and entries["F11"] == "Yes" and entries["F12"] == "Yes":
        inarow6.append(entries)
    #5 years in a row
    if entries["F08"] == "Yes" and entries["F09"] == "Yes" and entries["F10"] == "Yes" and entries["F11"] == "Yes" and entries["F12"] == "Yes":
        inarow5.append(entries)
    #etc.
    if entries["F09"] == "Yes" and entries["F10"] == "Yes" and entries["F11"] == "Yes" and entries["F12"] == "Yes":
        inarow4.append(entries)
    if entries["F10"] == "Yes" and entries["F11"] == "Yes" and entries["F12"] == "Yes":
        inarow3.append(entries)
    if entries["F11"] == "Yes" and entries["F12"] == "Yes":
        inarow2.append(entries)
    
print "Amount of tickets by year starting at 2012"
print len(F12)
print len(F11)
print len(F10)
print len(F09)
print len(F08)
print len(F07)
print "Amount in a row starting at 6"
print len(inarow6)
print len(inarow5)
print len(inarow4)
print len(inarow3)
print len(inarow2)

