#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(rows):
    """
    Returns a list of integers
    representing the Pascal Triangle of rows
    returns empty list if rows <= 0
    """
    triangle = []
    if rows <= 0:
        return triangle
    triangle = [[1]]
    for row in range(1, rows):
        new_row = [1]
        for col in range(len(triangle[row - 1]) - 1):
            previous_row = triangle[row - 1]
            new_row.append(previous_row[col] + previous_row[col + 1])
        new_row.append(1)
        triangle.append(new_row)
    return triangle
