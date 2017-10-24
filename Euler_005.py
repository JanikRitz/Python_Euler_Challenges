'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

import datetime
from caching import cache

start_time = datetime.datetime.now()

# Actual code

def next_prime(prev_primes):
    i = prev_primes[-1] + 2
    while 1:
        if is_prime(i, prev_primes):
            return i
        i += 2


@cache
def is_prime(number, prev_primes):
    for prime in prev_primes:
        if number % prime == 0:
            return False
    return True


primes = [2, 3, 5, 7, 11, 13]


@cache
def prime_fact(number):
    prime_fact = []
    while number > 1:
        for prime in primes:
            if number % prime == 0:
                prime_fact.append(prime)
                number /= prime
        primes.append(next_prime(primes))
    return prime_fact


def prime_fact_dic(number):
    prime_facts_list = prime_fact(number)
    prime_facts_dictionarie = {}
    for num in prime_facts_list:
        if num in prime_facts_dictionarie:
            prime_facts_dictionarie[num] += 1
        else:
            prime_facts_dictionarie[num] = 1
    return prime_facts_dictionarie


prime_facts = []
for i in range(2, 21):
    prime_facts.append(prime_fact_dic(i))

merged = {}

for primes in prime_facts:
    for prime in primes:
        if prime in merged:
            merged[prime] = max(primes[prime], merged[prime])
        else:
            merged[prime] = primes[prime]

least_mult = 1
for key in merged:
    least_mult *= key ** merged[key]

# End actual code
end_time = datetime.datetime.now()
print(f'Least multiple is: {least_mult} ({(end_time - start_time)})')
# Least multiple is: 232792560 (0:00:00)
