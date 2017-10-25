'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

import datetime

start_time = datetime.datetime.now()

# Actual code
maximum = 10 ** 6
lengths_cache = {}


def length(number: int) -> int:
    if number in lengths_cache:
        return lengths_cache[number]
    if number <= 1:
        return 1

    if number % 2 == 0:  # even
        l = length(int(number / 2)) + 1
    else:
        l = length(3 * number + 1) + 1
    lengths_cache[number] = l

    return l


best_length = max([(i, length(i)) for i in range(0, maximum + 1)], key=lambda x: x[1])

# End actual code
end_time = datetime.datetime.now()
print(f'Best Length is {best_length[1]}'
      f'from number {best_length[0]}'
      f'for a maximum of {maximum} ({(end_time - start_time)})')
# Best Length is 525 from number 837799 for a maximum of 1000000 (0:00:02.285432)
