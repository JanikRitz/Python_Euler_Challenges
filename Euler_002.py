'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

import datetime
import functools

start_time = datetime.datetime.now()
# Actual code

MAX = 4 * 10 ** 6


@functools.lru_cache(maxsize=10)
def fib(pos):
    if pos == 0:
        return 1
    if pos == 1:
        return 2
    return fib(pos - 1) + fib(pos - 2)


def fib_list(maximum):
    fibonacci = []
    i = 0
    while fib(i) < maximum:
        fibonacci.insert(i, fib(i))
        i += 1
    return fibonacci

sum_numbers = sum(filter(lambda x: x % 2 == 0, fib_list(MAX)))

# End actual code
end_time = datetime.datetime.now()
print(f'Sum: {sum_numbers} ({(end_time - start_time)})')
# 4613732
