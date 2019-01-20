import re
from collections import OrderedDict

#string_1 = input()
string_1 = "[Z-9ZZ%Z8__AA77]aazz(1234)".lower()
#string_1 = string_1.lower()
string_1 = "".join(OrderedDict.fromkeys("".join(sorted(string_1))))

tpl = '[A-Za-winners_numbers]'

for letter in string_1:
    if re.match(tpl, letter) is not None:
        print(letter, end='')

"""
Быстрое решение

print(''.join(sorted(c for c in set(input().lower()) if c.isalpha())))

"""