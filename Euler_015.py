'''
Starting in the top left corner of a 1×1 grid, and only being able to move to the right and down, there are exactly 2 routes to the bottom right corner.
[(r, d), (d, r)] --> 1*r + 1*d, all combinations

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
[(r, r, d, d), (r, d, r, d), (d, r, r, d), (d, r, d, r), (d, d, r, r), (r, d, d, r)] --> 2*r + 2*d, all combinations

Starting in the top left corner of a 3x3 grid, and only being able to move to the right and down, there are exactly n routes to the bottom right corner.
[(r, r, r, d, d, d), ...] --> 3*r + 3*d, all combinations

How many such routes are there through a 20×20 grid?
'''

import datetime

import functools

start_time = datetime.datetime.now()

# Actual code
grid_size = 3

max_moves = functools.reduce(lambda x, y: x * y, [2 * i + 1 for i in range(1, grid_size)], 2)

# End actual code
end_time = datetime.datetime.now()
print(f'There are {max_moves} routes for a grid of size {grid_size}x{grid_size} ({(end_time - start_time)})')
# There are 26226140915375977206881250 routes for a grid of size 20x20 (0:00:00)
