import re

with open('dataset_3363_2.txt', 'r') as inf:
    x = inf.readline().strip()

w = [value for value in re.findall("[a-zA-Z]*", x) if value != '']
n = [value for value in re.findall("[0-9]*", x) if value != '']

result = ''
for i in range(len(w)):
    result += w[i] * int(n[i])

with open('output.txt', 'w') as ans:
    ans.write(result)
