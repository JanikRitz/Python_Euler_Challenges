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

number_lengths ={
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3,
# ...
}

# End actual code
end_time = datetime.datetime.now()
print(f'When spelled the numbers from {start} to {end} use {number_chars} characters'
      f'(without spaces and hyphens) ({(end_time - start_time)})')
# There sum of the digits of 2^1000 is 1366 from ... (0:00:00.000999)
