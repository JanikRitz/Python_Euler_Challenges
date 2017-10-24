'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
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


number = 600851475143
primes = [2, 3, 5, 7, 11, 13]
prime_fact = []
while number > 1:
    for prime in primes:
        if number % prime == 0:
            prime_fact.append(prime)
            number /= prime
    primes.append(next_prime(primes))

max_prime = max(prime_fact)

# End actual code
end_time = datetime.datetime.now()
print(f'Sum: {max(prime_fact)} ({(end_time - start_time)})')
# 6857
