'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import datetime

start_time = datetime.datetime.now()

# Actual code

# primes = deque([2, 3, 5, 7, 11, 13])

limit = 2*10**6
numbers = set(range(3, limit, 2))
numbers.add(2)

for number in list(numbers):
    for value in range(number * 2, limit, number):
        if value in numbers:
            numbers.remove(value)
sum_primes = sum(numbers)


# End actual code
end_time = datetime.datetime.now()
print(f'Primenumbers below {limit} sum is: {sum_primes} ({(end_time - start_time)})')
# Primenumbers below 2000000 sum is: 142913828922 (0:00:01.761276)
