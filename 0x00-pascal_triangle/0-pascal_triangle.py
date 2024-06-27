#!/usr/bin/python3


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    tri_angle = []
    if n <= 0:
        return tri_angle
    tri_angle = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(tri_angle[i - 1]) - 1):
            curr = tri_angle[i - 1]
            temp.append(tri_angle[i - 1][j] + tri_angle[i - 1][j + 1])
        temp.append(1)
        tri_angle.append(temp)
    return tri_angle
