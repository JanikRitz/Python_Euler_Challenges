'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

import datetime

start_time = datetime.datetime.now()

# Actual code
max_moves = 0
grid_size = 20

# End actual code
end_time = datetime.datetime.now()
print(f'There are {max_moves} for a grid of size {grid_size}x{grid_size} ({(end_time - start_time)})')
# There are 0 for a grid of size 20x20 (0:00:00)
