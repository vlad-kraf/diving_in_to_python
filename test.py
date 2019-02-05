import datetime


"""
time = '20180315103842'
time = datetime.datetime.strptime(time,'%Y%m%d%H%M%S').weekday()
print(time)
"""

x = 2.0160303e+13
x = int(x)

print(type(x), str(x))






"""
import csv

csv_filename = "cars_week3.csv"
with open(csv_filename) as csv_fd:
    reader = csv.reader(csv_fd, delimiter=';')
    next(reader)  # пропускаем заголовок
    for row in reader:
        print(row)

"""

"""
import re
DATA = "8x3x2.5"
print (DATA.split('x'))
"""
