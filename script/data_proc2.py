from datetime import date
from datetime import datetime
import csv
resultado = {}

f = open("day_wise.csv", "r")

Y = 2000  # dummy leap year to allow input X-02-29 (leap day)
seasons = [('Winter', (date(Y,  1,  1),  date(Y,  3, 20))),
           ('Spring', (date(Y,  3, 21),  date(Y,  6, 20))),
           ('Summer', (date(Y,  6, 21),  date(Y,  9, 22))),
           ('Autumn', (date(Y,  9, 23),  date(Y, 12, 20))),
           ('Winter', (date(Y, 12, 21),  date(Y, 12, 31)))]


def get_season(now):
    if isinstance(now, datetime):
        now = now.date()
    now = now.replace(year=Y)
    return next(season for season, (start, end) in seasons
                if start <= now <= end)


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
        data.append('New Cases gt 5000')
        data.append('New Deaths gt 5000')
        data.append('New Recover gt 5000')
        data.append('Season')
    else:
        day = datetime.strptime(data[0], '%Y-%m-%d')
        data[0] = (day - first_day).days
        if int(data[5]) > 5000:
            data.append(1)
        else:
            data.append(0)
        if int(data[6]) > 5000:
            data.append(1)
        else:
            data.append(0)
        if int(data[7]) > 5000:
            data.append(1)
        else:
            data.append(0)
        data.append(get_season(day))
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
