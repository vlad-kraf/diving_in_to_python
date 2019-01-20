import sys
digit_string = sys.argv[1]

#digit_string = "873"

result = 0

for char in digit_string:
    digit = int(char)
    result = result + digit

print(result)

