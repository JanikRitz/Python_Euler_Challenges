'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import datetime

import itertools

start_time = datetime.datetime.now()

# Actual code
a, b, c = 0, 0, 0

for ab in itertools.permutations(range(100, 500), 2):
    a = ab[0]
    b = ab[1]
    c = 1000 - ab[0] - ab[1]
    if (a + b) < 1000 and a < b < c and a ** 2 + b ** 2 == c ** 2:
        break

# End actual code
end_time = datetime.datetime.now()
print(f'Pythagoran triplet is: {a, b, c} ({(end_time - start_time)})')
print(f'Pythagoran triplet product is : {a*b*c} ({(end_time - start_time)})')
# Pythagoran triplet is: (200, 375, 425) (0:00:00.115333)
# Pythagoran triplet product is : 31875000 (0:00:00.115333)
