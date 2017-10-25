'''
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

import datetime

start_time = datetime.datetime.now()

# Actual code
power = 1000

value = 2**power
sum_digits = sum([int(i) for i in str(value)])

# End actual code
end_time = datetime.datetime.now()
print(f'There sum of the digits of 2^{power} is {sum_digits} from {value} ({(end_time - start_time)})')
# There sum of the digits of 2^1000 is 1366 from ... (0:00:00.000999)
