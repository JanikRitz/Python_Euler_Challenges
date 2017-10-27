'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
'''

import datetime

start_time = datetime.datetime.now()

# Actual code
triangle = list()
max_routes = dict()
with open('Numbers_67.txt') as file:
    for line in file:
        triangle.append(tuple(map(lambda x: int(x), str(line).split(' '))))

triangle = tuple(triangle)

def max_route(triangle) -> int:
    if len(triangle) == 1:
        return triangle[0][0]

    if triangle in max_routes:
        return max_routes[triangle]

    left = max_route(left_sub_triangle(triangle))
    right = max_route(right_sub_triangle(triangle))
    max_routes[triangle] = triangle[0][0] + max(left, right)

    return max_routes[triangle]


def left_sub_triangle(triangle):
    sub_triangle = list()
    for row in triangle[1:]:
        sub_triangle.append(row[:-1])
    return tuple(sub_triangle)


def right_sub_triangle(triangle):
    sub_triangle = list()
    for row in triangle[1:]:
        sub_triangle.append(row[1:])
    return tuple(sub_triangle)


max_total = max_route(triangle)

# End actual code
end_time = datetime.datetime.now()
print(f'Maximum Total from top to bottom is {max_total} ({(end_time - start_time)})')
# Maximum Total from top to bottom is 7273 (0:00:00.176443)
