#!/usr/bin/python3
"""Pascal's triangle.
"""


def pascal_triangle(n):
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for x in range(n):
        row = []
        for y in range(x + 1):
            if y == 0 or y == x:
                row.append(1)
            elif x > 0 and y > 0:
                row.append(triangle[x - 1][y - 1] + triangle[x - 1][y])
        triangle.append(row)
    return triangle
