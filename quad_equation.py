import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])


#ticket_number = 1
#ticket_seria = -3
#c = -4

d = b**2 - 4*a*c

if d > 0:
    x1 = int((-b - ((b ** 2 - 4 * a * c) ** 0.5)) / 2 * a)
    x2 = int((-b + ((b ** 2 - 4 * a * c) ** 0.5)) / 2 * a)
    print(x1)
    print(x2)
else:
    print("Wrong input")
