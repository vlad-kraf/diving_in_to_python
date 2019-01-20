import string

def gen_ticket_number(count, series, length=6):
    """
    генератор номеров билетов, входные параметры: count - количество билетов,
    series - номер серии, необязательный аргумент length - количество цифр
    в номере, по умолчанию равен 6, выход - строка вида: <номер билета> <серия билета>
    """
    # напишите вашу реализацию здесь

    get_number = gen_number(length)
    get_series = gen_series(series)
    next_series = next(get_series)

    x = 1
    while x <= count:
        x = x + 1
        next_number = next(get_number)
        yield (str(next_number) + ' ' + str(next_series))
        if int(next_number) == int('9' * length):
            get_number = gen_number(length)
            next_series = next(get_series)
    pass


def gen_series(series):
    """
    генератор серий лотерейных билетов, входные параметры: series -- номер серии,
    выход - строка, состоящая из двух заглавных букв латинского алфавита
    """
    # напишите вашу реализацию здесь
    series = series.upper()

    alphabet = string.ascii_uppercase

    index_1 = alphabet.find(series[0])
    index_2 = alphabet.find(series[1])

    for j in range(index_1, 26):
        for i in range(index_2, 26):
            yield (alphabet[j] + '' + alphabet[i])

    pass


def gen_number(length=6):
    """
    генератор номеров лотерейных билетов, входные параметры: необязательный
    аргумент length - количество цифр в номере, по умолчанию равен 6
    """
    # напишите вашу реализацию здесь

    max_number = int('9' * length)

    a = ((str(i + 1).zfill(length)) for i in range(max_number))

    return a
    pass

