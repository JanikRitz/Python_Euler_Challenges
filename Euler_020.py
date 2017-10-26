'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

import datetime

import functools

start_time = datetime.datetime.now()

# Actual code
start = 1
stop = 100
sum_of_digits = sum([int(i) for i in str(int(functools.reduce(lambda x, y: x * y, range(start, stop + 1))))])

# End actual code
end_time = datetime.datetime.now()
print(f'The sum of the digits of {stop}! is {sum_of_digits} ({(end_time - start_time)})')
# The sum of the digits of 100! is 648 (0:00:00.000501)
