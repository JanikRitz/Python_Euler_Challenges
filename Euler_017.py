'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

import datetime

start_time = datetime.datetime.now()

# Actual code
number_chars = 0
start = 1
end = 1000

numbers_spec = {
    10: 'Ten',
    11: 'Eleven',
    12: 'Twelve',
    13: 'Thirteen',
    14: 'Fourteen',
    15: 'Fifteen',
    16: 'Sixteen',
    17: 'Seventeen',
    18: 'Eighteen',
    19: 'Nineteen',
}

numbers_1 = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
}

numbers_2 = {
    2: 'Twenty',
    3: 'Thirty',
    4: 'Forty',
    5: 'Fifty',
    6: 'Sixty',
    7: 'Seventy',
    8: 'Eighty',
    9: 'Ninety',
}


def number_as_text(number: int) -> str:
    if number in numbers_spec:
        return numbers_spec[number]

    if len(str(number)) == 4:
        extra = ''
        if not int(str(number)[1:]) == 0:
            extra = f' and {number_as_text(int(str(number)[1:]))}'
        return f'{number_as_text(int(str(number)[0]))} thousand{extra}'

    if len(str(number)) == 3:
        extra = ''
        if not int(str(number)[1:]) == 0:
            extra = f' and {number_as_text(int(str(number)[1:]))}'
        return f'{number_as_text(int(str(number)[0]))} hundred{extra}'

    if len(str(number)) == 2:
        extra = ''
        if not int(str(number)[1:]) == 0:
            extra = f'-{number_as_text(int(str(number)[1:]))}'
        return f'{numbers_2[int(str(number)[0])]}{extra}'

    if len(str(number)) == 1:
        return numbers_1[number]

    raise ValueError


def length_number(number: str) -> int:
    number = number.replace(' ', '')
    number = number.replace('-', '')
    return len(number)


for i in range(start, end + 1):
    number_chars += length_number(number_as_text(i))

# End actual code
end_time = datetime.datetime.now()
print(f'When spelled the numbers from {start} to {end} use {number_chars} characters'
      f'(without spaces and hyphens) ({(end_time - start_time)})')
# There sum of the digits of 2^1000 is 1366 from ... (0:00:00.000999)
