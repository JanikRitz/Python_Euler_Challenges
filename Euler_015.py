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

start_time = datetime.datetime.now()

# Actual code
stored_routes = dict()
grid_size = 20


def routes(size: (int, int)) -> int:
    s_size = (min(size), max(size))
    n, m = s_size

    # Negative Value
    if n < 0:
        raise ValueError

    if s_size in stored_routes:
        return stored_routes[s_size]

    # No Field
    if n == m == 0:
        return 0

    # Just a Line
    if n == 0:
        return 1

    # Simple narrow Field
    if n == 1:
        return m + 1

    # Quadratic Field
    if n == m:
        return sum([routes((n - i, i)) ** 2 for i in range(n + 1)])
    
    return sum([routes((n-i, i)) * routes((i, m-i)) for i in range(n + 1)])


max_moves = routes((grid_size, grid_size))

# End actual code
end_time = datetime.datetime.now()
print(f'There are {max_moves} routes for a grid of size {grid_size}x{grid_size} ({(end_time - start_time)})')
# There are 137846528820 routes for a grid of size 20x20 (0:00:00.006998)
