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

from caching import Cache
from tqdm import tqdm

start_time = datetime.datetime.now()

# Actual code
result = "Result"


def chain(a: int, b: int):
    def quadratic(n):
        return n ** 2 + a * n + b

    for n in range(10 ** 10):
        if not is_prime(quadratic(n)):
            return n
    return 0


@Cache(maxsize=-1)
def is_prime(number):
    if number % 2 == 0 or number == 1:
        return False
    for test in range(3, int(number / 2), 2):
        if number % test == 0:
            return False
    return True


a_max = 1000
b_max = 1000

chains = map(lambda x: (chain(x[0], x[1]), x[0], x[1]),
             itertools.product(range(-a_max, a_max), range(-b_max - 1, b_max + 1)))
max_chain = (0, 0, 0)
for test_chain in tqdm(chains, total=a_max * b_max * 4):
    if test_chain[0] > max_chain[0]: max_chain = test_chain

# key=lambda element: element[2])
print(max_chain)
# End actual code
end_time = datetime.datetime.now()

print(f'Result is {chain(1, 41)} ({(end_time - start_time)})')
# Result
