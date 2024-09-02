#!/usr/bin/python3
"""
Module that contains a function to calculate the perimeter of an island
represented in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    The grid represents a map where:
    - 0 represents water
    - 1 represents land

    Cells are connected horizontally/vertically (not diagonally). The grid is 
    completely surrounded by water, and there is exactly one island (one or more 
    connected land cells).

    Parameters:
    grid (List[List[int]]): A list of lists where each sublist represents a row 
                            of the grid.

    Returns:
    int: The perimeter of the island.
    """
    # Set to keep track of visited land cells
    visit = set()

    def dfs(i, j):
        """
        Depth-first search to explore the island and calculate the perimeter.

        Parameters:
        i (int): The row index of the cell.
        j (int): The column index of the cell.

        Returns:
        int: The perimeter contribution of the current cell.
        """
        # If the cell is out of bounds or is water, it contributes to the perimeter
        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
            return 1
        # If the cell is already visited, it doesn't contribute further
        if (i, j) in visit:
            return 0

        # Mark the cell as visited
        visit.add((i, j))
        
        # Check all four directions (right, down, left, up) and sum up perimeter contributions
        perim = dfs(i, j + 1)  # right
        perim += dfs(i + 1, j) # down
        perim += dfs(i, j - 1) # left
        perim += dfs(i - 1, j) # up
        return perim

    # Iterate through the grid to find the first land cell and start DFS
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Start DFS only on land cells
            if grid[i][j] == 1:
                return dfs(i, j)

    # If no land cells are found, the perimeter is 0
    return 0
