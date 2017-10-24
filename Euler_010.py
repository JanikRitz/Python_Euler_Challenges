'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import datetime

start_time = datetime.datetime.now()

# Actual code

# primes = deque([2, 3, 5, 7, 11, 13])


def primes_gen(max_prime):
    primes = [2, 3, 5, 7, 11, 13]
    for prime in primes:
        if prime < limit:
            yield prime
    prime = primes[-1]
    while prime < max_prime:
        prime += 2
        if is_prime_cached(prime, primes):
            primes.append(prime)
            yield prime


def is_prime_cached(number, prev_primes):
    for prime in prev_primes:
        if number % prime == 0:
            return 1
    return 0


def is_prime(number):
    if number%2 == 0 or number == 1:
        return 0
    for test in range(3, int(number/2),2):
        if number%test == 0:
            return 0
    return number



for i in range(0, 7):
    start_time = datetime.datetime.now()
    limit = 2 * 10 ** i

    primes_sum = sum(map(is_prime, list(range(1, limit, 2))))+2
    end_time = datetime.datetime.now()
    print(f'Primenumbers below {limit} sum is: {primes_sum} ({(end_time - start_time)})')

# End actual code
end_time = datetime.datetime.now()
print(f'Primenumbers below {limit} sum is: {primes_sum} ({(end_time - start_time)})')
# Primenumbers below 2000000 sum is: 142913828922 (0:44:13.534106)
# Primenumbers below 2000000 sum is: 142913828922 (0:44:33.280444)
# Primenumbers below 2000000 sum is: 142913828922 (0:44:56.335723)
