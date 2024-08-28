#!/usr/bin/python3
"""Defines island perimeter finding function."""


def island_perimeter(grid):
    """Return the perimiter of an island.
    The grid represents water by 0 and land by 1.
    Args:
        grid (list): A list of list of integers representing an island.
    Returns:
        The perimeter of the island defined in grid.
    """
    num_columns = len(grid[0])
    num_rows = len(grid)
    shared_edges = 0
    land_cells = 0

    for i in range(num_rows):
        for j in range(num_columns):
            if grid[i][j] == 1:
                land_cells += 1
                if (j > 0 and grid[i][j - 1] == 1):
                    shared_edges += 1
                if (i > 0 and grid[i - 1][j] == 1):
                    shared_edges += 1
    return land_cells * 4 - shared_edges * 2
