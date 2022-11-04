'''
Number of Islands
https://leetcode.com/problems/number-of-islands/

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None or len(grid) == 0:
            return 0
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid
        res = 0
        for i in range(self.rows):
            for j in range(self.cols):
                res += self.dfs(i, j)
        return res
    def dfs(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols and self.grid[row][col] == '1':
            self.grid[row][col] = '0'
            self.dfs(row - 1, col)
            self.dfs(row + 1, col)
            self.dfs(row, col - 1)
            self.dfs(row, col + 1)
            return 1
        else:
            return 0

#**********************************
#*********** VERSION 2 ************
#**********************************

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None or len(grid) == 0:
            return 0
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid
        return sum(self.dfs(i, j) for i in range(self.rows) for j in range(self.cols))
    def dfs(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols and self.grid[row][col] == '1':
            self.grid[row][col] = '0'
            list(map(self.dfs, (row-1, row+1, row, row), (col, col, col-1, col+1)))
            return 1
        return 0

#**********************************
#*********** VERSION 3 ************
#**********************************

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None or len(grid) == 0:
            return 0
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid
        return sum(self.grid[i][j] == '1' and not self.dfs(i, j) for i in range(self.rows) for j in range(self.cols))
    def dfs(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols and self.grid[row][col] == '1':
            self.grid[row][col] = '0'
            list(map(self.dfs, (row-1, row+1, row, row), (col, col, col-1, col+1)))

#**********************************
#*********** VERSION 4 ************
#**********************************

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None or len(grid) == 0:
            return 0
        def dfs(row, col):
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == '1':
                grid[row][col] = '0'
                list(map(dfs, (row-1, row+1, row, row), (col, col, col-1, col+1)))
        rows = len(grid)
        cols = len(grid[0])
        return sum(grid[i][j] == '1' and not dfs(i, j) for i in range(rows) for j in range(cols))
