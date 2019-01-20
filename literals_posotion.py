import re
from collections import OrderedDict

string_1 = input()
string_2 = input()
string_1 = string_1.lower()
string_2 = string_2.lower()
string_2 = "".join(OrderedDict.fromkeys(string_2))
tpl = '[A-Za-winners_numbers]'

for letter in string_2:
    if re.match(tpl, letter) is not None:
        print(letter, end=' ')
        if letter in string_1:
            for match in re.finditer(letter, string_1):
                print(match.start()+1, end=' ')
        else:
            print(None, end=' ')
        print("")
    else:
        pass

"""
Быстрое решение:

s1 = input().lower()
s2 = input().lower()
checked = set()
for ch in s2:
    if ch.isalpha() and ch not in checked:
        checked.add(ch)
        indices = ' '.join(str(i+1) for i,v in enumerate(s1) if v == ch)
        print(ch, indices or 'None')

"""