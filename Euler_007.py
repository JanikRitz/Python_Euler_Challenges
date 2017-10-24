'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

import datetime

start_time = datetime.datetime.now()


# Actual code

def next_prime(prev_primes):
    i = prev_primes[-1] + 2
    while 1:
        if is_prime(i, prev_primes):
            return i
        i += 2


def is_prime(number, prev_primes):
    for prime in prev_primes:
        if number % prime == 0:
            return False
    return True


primes = [2, 3, 5, 7, 11, 13]
for i in range(0, 10001 - len(primes)):
    primes.append(next_prime(primes))

# End actual code
end_time = datetime.datetime.now()
print(f'10.001st prime number: {primes[10000]} ({(end_time - start_time)})')
# 104743
