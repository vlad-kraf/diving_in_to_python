import sys
num_steps = int(sys.argv[1])

#num_steps = int(5)

i = 0
j = num_steps
while i < num_steps:
    i += 1
    j -= 1
    print(" "*j + "#"*i)

