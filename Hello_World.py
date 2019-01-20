import random


number = random.randint(0, 101)

while  True:
    answear = input("Введите число: ")
    if not answear or answear == "exit":
        break

    if not answear.isdigit():
        print("Введите правильное число")
        continue

    user_answear = int(answear)

    if user_answear > number:
        print("Загаданное число меньше")
    elif user_answear < number:
        print("Загаданное число больше")
    else:
        print("Угадал")
        break