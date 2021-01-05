from datetime import date
from datetime import datetime
import csv
resultado = {}

f = open("day_wise.csv", "r")

# Get the first date for normalize the data
with open('day_wise.csv') as csv_data:
    reader = csv.reader(csv_data, delimiter=',')
    next(reader)
    days_sorted = sorted(reader, key=lambda data: datetime.strptime(
        data[0], '%Y-%m-%d'), reverse=False)

first_day = datetime.strptime(days_sorted[0][0],  '%Y-%m-%d')

for line in f.readlines():
    data = line.split(',')

    key = data[0]  # group by date

    if data[0] == 'Date':
        data.append('New Cases gt 1000')
        data.append('New Deaths gt 1000')
    else:
        day = datetime.strptime(data[0], '%Y-%m-%d')
        data[0] = (day - first_day).days
        if int(data[5]) > 1000:
            data.append(1)
        else:
            data.append(0)
        if int(data[6]) > 1000:
            data.append(1)
        else:
            data.append(0)
    i = 0
    res = ''
    while i < len(data):
        res = res + str(data[i])
        i = i+1
        if i < len(data):
            res = res + ','
    # Delete the lines break
    res = res.replace('\n', ' ').replace('\r', '')
    resultado[key] = res

p = open("../datos_nuevos_casos/regresion_train.csv", "w")
for line in resultado:
    p.write(resultado[line] + "\n")
