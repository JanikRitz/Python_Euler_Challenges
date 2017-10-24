'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import datetime

# Actual code

# primes = deque([2, 3, 5, 7, 11, 13])


sieve = set()
print("Sum of primes less than...?")
i = int(input())

start_time = datetime.datetime.now()

psum = (i * (i + 1)) / 2


def S(x):
    n = 2
    m = 2
    while n <= round(x ** .5):
        if m * n <= i:
            sieve.add(m * n)
            m += 1
        else:
            m = 2
            n += 1


S(i)
print(sum(sieve))
psum = psum - sum(sieve)

# End actual code
end_time = datetime.datetime.now()
print(f'Primenumbers below {i} sum is: {psum-1} ({(end_time - start_time)})')
# Primenumbers below 2000000 sum is: 142913828922.0 (0:00:09.010722)
