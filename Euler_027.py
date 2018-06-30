'''
Euler discovered the remarkable quadratic formula:

n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
'''

import datetime
import itertools
import math

from caching import Cache
from tqdm import tqdm

start_time = datetime.datetime.now()

# Actual code
result = "Result"


def chain(a: int, b: int, cur_max=0):
    if a % b == 0 and b < cur_max:
        return 0

    for n in range(10 ** 4):
        if not is_prime(n ** 2 + a * n + b):
            return n
    return 0


def prime_list(upper_bound):
    primes = [2] + list(range(3, upper_bound, 2))
    for i in range(upper_bound):
        primes = list(filter(lambda x: x == primes[i] or x % primes[i] != 0, primes))
        if i > math.sqrt(upper_bound):
            return primes


primes_test_max = 10 ** 5
primes_test = prime_list(primes_test_max)


@Cache(maxsize=-1)
def is_prime(number):
    if number <= primes_test_max:
        return number in primes_test
    for test in primes_test:
        if number % test == 0:
            return False
        if test > math.sqrt(number):
            return True
    return True


a_max = 1000
b_max = 1000

# Use primes for b for better runtime
# if n=0 it tests for b as prime
# if n=1 a must be uneven, because b and 1 are uneven and the result has to be uneven
range_a = range(-a_max + 1, a_max, 2)
range_b = prime_list(b_max)
range_b += list(map(lambda x: -x, range_b))
combinations = itertools.product(range_a, range_b)

max_chain = (0, 0, 0)
for combination in tqdm(combinations, total=a_max * len(range_b)):
    test_chain = (chain(combination[0], combination[1], max_chain[0]), combination[0], combination[1])
    if test_chain[0] > max_chain[0]:
        max_chain = test_chain

# End actual code
end_time = datetime.datetime.now()

print(f'The quadratic formula n^2 + ({max_chain[1]})*n + ({max_chain[2]})'
      f' has a chain length of {max_chain[0]}'
      f' and the factor a*b is {max_chain[1]*max_chain[2]} ({(end_time - start_time)})')
# The quadratic formula n^2 + (-61)*n + (971) has a chain length of 71 and the factor a*b is -59231 (0:00:09.705505)
