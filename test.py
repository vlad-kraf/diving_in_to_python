import collections
text = 'TABLE OF CONTENT\nJanuary:1\nFebruary:33\n'
table = collections.OrderedDict()

words = text.split("\n")

for word in words:
    temp = word.split(":")

    if len(temp) == 1:
        value = ''
        table[temp[0]] = value
    else:
        table[temp[0]] = temp[1]





for key  in table:
    if table[key] == '':
        print(key)
    else:
        print(key+":"+table[key])

print(table['sdf'])