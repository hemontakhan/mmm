import csv
with open('height-weight.csv',newline='') as x:
    observe = csv.reader(x)
    data_chart = list(observe)

data_chart.pop(0)

pol_data = []

for a in range(len(data_chart)):
    num_n = data_chart[a][1]
    pol_data.append(float(num_n))

y = len(pol_data)
total = 0
for z in pol_data:
    total += z 

average = total/y

print("AVERAGE OR MEAN OF THE DATA IS "+str(average))