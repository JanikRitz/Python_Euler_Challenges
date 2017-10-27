'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import datetime

start_time = datetime.datetime.now()

# Actual code
max_value = 10000
sum_amicable = 0

# End actual code
end_time = datetime.datetime.now()
print(f'The sum of all amicable numbers below {max_value} is {sum_amicable} ({(end_time - start_time)})')
# The sum of all amicable numbers below 10000 is 0 (0:00:00)
