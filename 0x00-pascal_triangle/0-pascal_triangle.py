#!/usr/bin/python3
"""
    Pascal triangle
"""


def pascal_triangle(n):

    """Create a func for pascal_triangle"""
    if n <= 0:
        return []
    tri = [[1]]

    for i in range(1, n):
        row = tri[-1]
        current_row = [1]
        for j in range(1, i):
            current_row.append(row[j - 1] + row[j])
        current_row.append(1)
        tri.append(current_row)
    return tri
