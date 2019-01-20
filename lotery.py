"""

cnt_winners = int(input())
ticket_number, ticket_seria = map(str, input().split())
cnt_tickets = ''
ticket_seria = ticket_seria.upper()
cnt_tickets = re.sub('[0]', '', ticket_number)
cnt_tickets = int(cnt_tickets)



if cnt_winners < int(ticket_number):
    winners_numbers = random.sample(range(1, cnt_tickets+1), cnt_winners)
    ticket = ''
    j = 0
    k = cnt_winners
    while j < cnt_winners:
        i = 0
        ticket = ''
        while i < (len(ticket_number) - (len(str(winners_numbers[j - 1])))):
            ticket += '0'
            i += 1

        ticket += (str(winners_numbers[j - 1]) + ' ' + ticket_seria)
        print(f"Победитель номер {k} - \"{ticket}\"")
        j += 1
        k -= 1
else:
    winners_numbers = random.sample(range (1, int(ticket_number)+1), int(ticket_number))
    ticket = ''
    j = 0
    k = int(ticket_number)
    while j < int(ticket_number):
        i = 0
        ticket = ''
        while i < (len(ticket_number) - (len(str(winners_numbers[j - 1])))):
            ticket += '0'
            i += 1

        ticket += (str(winners_numbers[j - 1]) + ' ' + str(ticket_seria))

        print(f"Победитель номер {k} - \"{ticket}\"")
        j += 1
        k -= 1


Быстрое решение:
"""
import random
count = int(input())
number, series = input().upper().lstrip('0').split()
count = min(count, int(number))
winners = random.sample(range(1, int(number) +1), count)

for count, num in enumerate(winners, 1):
    print(f'Победитель номер {count} - "{num:06} {series}"') 







