#!/usr/bin/python3

""" island perimeter solution """


def island_perimeter(grid):
    """global function for island"""
    visit = set()

    def dfs(i, j):
        """function for testing the island"""
        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
            return 1
        if (i, j) in visit:
            return 0
        visit.add((i, j))
        perim = dfs(i, j + 1)
        perim += dfs(i + 1, j)
        perim += dfs(i, j - 1)
        perim += dfs(i - 1, j)
        """ return perim """
        return perim

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                """return the dfs function"""
                return dfs(i, j)
    """ If no land cells are found, the perimeter is 0 """
    return 0
