'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

import datetime

import itertools

from Euler_Amicable import number_form, NumberForm, proper_divisors

start_time = datetime.datetime.now()

# Actual code
min_test = 24
max_test = 28123

abundant_numbers = list(filter(lambda x: number_form(x) == NumberForm.ABUNDANT, range(3, min_test)))


def has_abundant_sum(number: int) -> bool:
    if number_form(number) == NumberForm.ABUNDANT:
        abundant_numbers.append(abundant_numbers)
    if number in map(lambda x: x[0]+x[1], itertools.combinations(abundant_numbers, 2)):
        return True
    return False

print(list(map(lambda x: x,itertools.combinations(abundant_numbers, 2))))
total = sum(itertools.filterfalse(has_abundant_sum, range(min_test, max_test + 1)))

# End actual code
end_time = datetime.datetime.now()
print(f'The sum of all the positive integers which cannot'
      f'be written as the sum of two abundant numbers is {total} ({(end_time - start_time)})')
# The total of all the name scores is 871198282 (0:00:00.017000)
