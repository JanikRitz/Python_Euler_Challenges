'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

import datetime

start_time = datetime.datetime.now()

# Actual code
size = 1001
# 01
# 4*(3^2) - 6*(3-1) = 24
# 4*(5^2) - 6*(5-1) = 76

sum_diagonals = 1 + sum(map(lambda n: 4 * n ** 2 - 6 * (n - 1), range(3, size + 1, 2)))

# End actual code
end_time = datetime.datetime.now()

print(f'Sum of diagonals is {sum_diagonals} in a square of size {size}x{size} ({(end_time - start_time)})')
# Result
