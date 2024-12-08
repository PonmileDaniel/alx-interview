#!/usr/bin/python3
"""
Calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in the grid.

    Args:
        grid (list of list of int): 2D grid representing the map.

    Returns:
        int: Perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Add 4 for the current cell
                perimeter += 4

                # Check the above cell
                if row > 0 and grid[row-1][col] == 1:
                    perimeter -= 1

                # Check the below cell
                if row < rows - 1 and grid[row+1][col] == 1:
                    perimeter -= 1

                # Check the left cell
                if col > 0 and grid[row][col-1] == 1:
                    perimeter -= 1

                # Check the right cell
                if col < cols - 1 and grid[row][col+1] == 1:
                    perimeter -= 1

    return perimeter
