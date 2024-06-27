#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    triang = []
    if n <= 0:
        return triang
    triang = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(triang[i - 1]) - 1):
            curt = triang[i - 1]
            temp.append(triang[i - 1][j] + triang[i - 1][j + 1])
        temp.append(1)
        triang.append(temp)
    return triang
