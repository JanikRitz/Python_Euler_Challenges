'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

import datetime

start_time = datetime.datetime.now()

# Actual code
index = 0


def fib():
    yield 1
    yield 1
    fib_1 = 1
    fib_2 = 1
    while True:
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        yield fib_2


for index, fibonacci in enumerate(fib()):
    if len(str(fibonacci)) == 1000:
        index += 1
        break

# End actual code
end_time = datetime.datetime.now()

print(f'Index of first Fibonacci with 1000 digits is {index} ({(end_time - start_time)})')
# Index of first Fibonacci with 1000 digits is 4782 (0:00:00.049318)
