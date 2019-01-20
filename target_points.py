import re
shots_count = int(input("Введите кол-во выстрелов: "))

x1 = 0
y1 = 0
Sample_Output = 0

for i in range(shots_count):
    string = str(input("Введите координаты: "))
    str1 = re.search('(.*) ', string)
    str2 = re.search(' (.*)', string)

    x2 = abs(float(str1.group(1)))
    y2 = abs(float(str2.group(1)))


#    x2 = abs(float(row[0]))
#    y2 = abs(float(row[0]))
    r = (((x2 - x1)**2) + ((y2-y1)**2))**0.5
    if 0 <= r < 1:
        points = 10
    elif 1 <= r < 2:
        points = 9
    elif 2 <= r < 3:
        points = 8
    elif 3 <= r < 4:
        points = 7
    elif 4<= r < 5:
        points = 6
    elif 5 <= r < 6:
        points = 5
    elif 6 <= r < 7:
        points = 4
    elif 7 <= r < 8:
        points = 3
    elif 8<= r < 9:
        points = 2
    elif 9 <= r < 10:
        points = 1
    else: points = 0

    Sample_Output = Sample_Output + points

print(Sample_Output)


"""
Бфстрое решение:

points = 0
k = int(input())
shots = list(tuple(map(float, input().split())) for _ in range(k))
if k:
    grade = [i ** 2 for i in range(1, 11)]
    for x, y in shots:
        shot = x ** 2 + y ** 2
        points += sum(shot < point for point in grade)
print(points)

"""