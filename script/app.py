resultado = {}

f = open("real_datos.csv", "r")
for line in f.readlines():
    data = line.split(',')

    key = data[1] # group by date
    if key in resultado:

        d = resultado[key].split(',')
        if not "," in data[5] and not ':' in data[5]:
            d[3] = str(int(float(d[3])) + int(float(data[5]))) #Confirmed
            d[4] = str(int(float(d[4])) + int(float(data[6]))) #Deaths
            resultado[key] = ",".join(d)
    else:
        if not "," in data[5] and not ':' in data[5]:
            resultado[key] = data[1]+","+data[2]+","+data[3]+","+data[5]+","+data[6]

p = open("../datos/regresion_train.csv", "w")
for line in resultado:
    p.write(resultado[line] + "\n")
