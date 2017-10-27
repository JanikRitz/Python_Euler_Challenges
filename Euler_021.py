'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import datetime

import itertools

start_time = datetime.datetime.now()

# Actual code
max_value = 10000
cache_sum_proper_divisors = dict()


def proper_divisors(number: int) -> int:
    yield 1
    square_root = int(number ** 0.5)
    if number % square_root == 0:
        yield square_root
    for i in range(2, square_root + 1):
        if number % i == 0:
            yield i
            yield int(number / i)


def sum_proper_divisors(number: int) -> int:
    if number in cache_sum_proper_divisors:
        return cache_sum_proper_divisors[number]
    cache_sum_proper_divisors[number] = sum(proper_divisors(number))
    return cache_sum_proper_divisors[number]


def amicable(numbers: (int, int)) -> bool:
    if numbers[0] == numbers[1]:
        return False
    if sum_proper_divisors(numbers[0]) == numbers[1] and sum_proper_divisors(numbers[1]) == numbers[0]:
        return True
    return False


def gen_amicable(number: int) -> (int, int) or None:
    pair = (number, sum_proper_divisors(number))
    if amicable(pair):
        return pair


amicable_pairs = list(filter(gen_amicable, range(3, max_value)))
sum_amicable = sum(amicable_pairs)

# End actual code
end_time = datetime.datetime.now()
print(f'The sum of all amicable numbers below {max_value} is {sum_amicable} ({(end_time - start_time)})')
# The sum of all amicable numbers below 10000 is 0 (0:00:00)
