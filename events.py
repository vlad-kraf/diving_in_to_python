import csv
import datetime


# Convert csv to list
def data_creator(csv_filename="events_log.csv"):
    data = list()

    with open(csv_filename) as csv_fd:
        reader = csv.DictReader(csv_fd, delimiter=',')

        for row in reader:
            data.append(row)

    return data


data = data_creator()


# Пример. Считаем сумму по колонке checkin
def sum_columns(name='checkin'):
    sum_col = 0
    for i in range(len(data)):
        if data[i][name] != 'NA':
            sum_col = sum_col + int(data[i][name])
    return sum_col


# 3. What is the daily overall zero results rate? How does it vary between the groups?
zero_results_a = dict()
zero_results_b = dict()

for i in range(len(data)):
    if data[i]['group'] == 'a':
        time = str(data[i]['timestamp'])

        time = datetime.datetime.strptime(str(int(float(time))), '%Y%m%d%H%M%S').weekday()
        if data[i]['n_results'] == 'NA':
            zero_results_a[time] = zero_results_a.get(time, 0) + 1

    elif data[i]['group'] == 'b':
        time = str(int(data[i]['timestamp']))

        time = datetime.datetime.strptime(str(int(float(time))), '%Y%m%d%H%M%S').weekday()
        if data[i]['n_results'] == 'NA':
            zero_results_b[time] = zero_results_b.get(time, 0) + 1

    else:
        pass

print("group_a", sorted(zero_results_a.items()))
print("group_b", sorted(zero_results_b.items()))

 
"""
print(data[0])
print(data[0]['checkin'])
print(type(data[2]['checkin']))
print(data[400164]['uuid'])
print(len(data))
print(sum_columns('checkin'))

"""


