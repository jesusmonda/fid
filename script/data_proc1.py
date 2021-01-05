from datetime import date
from datetime import datetime
import csv
resultado = {}

f = open("real_datos.csv", "r")

# Get the first date for normalize the data
with open('real_datos.csv') as csv_data:
    reader = csv.reader(csv_data, delimiter=',')
    next(reader)
    days_sorted = sorted(reader, key=lambda data: datetime.strptime(
        data[1], '%m/%d/%Y'), reverse=False)

first_day = datetime.strptime(days_sorted[0][1],  '%m/%d/%Y')

for line in f.readlines():
    data = line.split(',')

    key = data[1]  # group by date
    if key in resultado:

        d = resultado[key].split(',')
        if not "," in data[5] and not ':' in data[5]:
            d[3] = str(int(float(d[3])) + int(float(data[5])))  # Confirmed
            d[4] = str(int(float(d[4])) + int(float(data[6])))  # Deaths
            resultado[key] = ",".join(d)
    else:
        if data[1] != 'ObservationDate':
            day = datetime.strptime(data[1],  '%m/%d/%Y')
            data[1] = (day - first_day).days

        if not "," in data[5] and not ':' in data[5]:
            resultado[key] = str(data[1])+","+data[2] + \
                ","+data[3]+","+data[5]+","+data[6]

p = open("../datos/regresion_train.csv", "w")
for line in resultado:
    p.write(resultado[line] + "\n")
