'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
import datetime

import itertools


# Actual code
def is_palindrome(text: str) -> bool:
    for i in range(0, int(len(text) / 2)):
        if text[i] != text[-i - 1]:
            return False
    return True


def is_palindrome_int(number: int) -> bool:
    return is_palindrome(str(number))


def high_combo(max, min):
    for i in range(max, min, -1):
        for tup in enumerate(itertools.permutations(range(max, i, -1), 2)):
            yield tup

'''
9, 9 = 81
9, 8 = 72
8,8 0 64



entries = set()
for tup in high_combo(10,0):
    print(tup, tup[1][0]*tup[1][1])
exit()
'''


def yield_pals(maximum, minimum):
    n1, n2, mult = 0, 0, 0
    for tup in enumerate(itertools.permutations(range(maximum, minimum, -1), 2)):
        n1, n2 = tup[1][0], tup[1][1]
        mult = n1 * n2
        if is_palindrome_int(mult):
            yield mult, n1, n2

start_time = datetime.datetime.now()

maximum = 0
try:
    maximum = max(yield_pals(999, 900))
except ValueError:
    pass
if maximum:
    print(maximum)

# End actual code
end_time = datetime.datetime.now()
print(f'Largest Palindrome: {maximum} ({(end_time - start_time)})')
# (906609, 993, 913)
