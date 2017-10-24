'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

import datetime

start_time = datetime.datetime.now()


# Actual code

def square_gen(min, max):
    for i in range(min, max):
        yield i ** 2


sum_squares = sum(square_gen(1, 101))
square_sum = sum(range(1, 101)) ** 2
difference = square_sum - sum_squares

# End actual code
end_time = datetime.datetime.now()
print(f'The difference is: {square_sum} - {sum_squares} = {difference} ({(end_time - start_time)})')
# The difference is: 25502500 - 338350 = 25164150 (0:00:00)
