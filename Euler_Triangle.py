max_routes = dict()


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