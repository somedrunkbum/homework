#!/usr/bin/python
# coding=utf-8
import csv, sys
from datetime import datetime


file = sys.argv[1]
rubl = 70
money_spend = 0
gas_spent = 0
date_format = "%m/%d/%Y"

with open(file) as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        if row[5] == 'RUR':
            money = int(row[3]) * rubl
        else:
            money = int(row[3])
        money_spend += money
        if row[2]:
            gas = float(row[2])
        gas_spent += gas
    print reader[1]
    #a = datetime.strptime('8/18/2008', date_format)
    #b = datetime.strptime('9/26/2008', date_format)
    #delta = b - a

print ('Money spend: {}'.format(money_spend))
print ('Total gas spend: {}'.format(gas_spent))
#print delta.days
#print a