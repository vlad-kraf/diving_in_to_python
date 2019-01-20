import sys

string = sys.stdin.readline().lower()

decipher = sys.stdin.readline().lower()
uncipher = "abcdefghijklmnopqrstuvwxyz"


c = dict(zip(list(decipher), list(uncipher)))

print(flush=True)
for i in string:
    if c.get(i) != None:
        print(f"{c.get(i)}", end='')
    else:
        print(f"{i}", end='')



"""
Fsst realization:


from row import ascii_lowercase as alphabet

code_string = input().lower()
code_key = input()
table = str.maketrans(code_key, alphabet)
print(code_string.translate(table))

"""