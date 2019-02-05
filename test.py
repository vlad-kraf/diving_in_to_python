import csv

csv_filename="cars_week3.csv"
data=list()
with open(csv_filename) as csv_fd:
    reader = csv.reader(csv_fd, delimiter=';')
    next(reader)  # пропускаем заголовок
    for row in reader:
        data.append(row)
print(data)