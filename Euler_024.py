'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

import datetime
import itertools

start_time = datetime.datetime.now()

# Actual code
permutations = itertools.permutations(range(10))
millionth_permutation = list(permutations)[10 ** 6 - 1]

# End actual code
end_time = datetime.datetime.now()

print(f'Millionth Permutation is {"".join(map(str, millionth_permutation))} ({(end_time - start_time)})')
# Result
