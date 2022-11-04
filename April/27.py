'''
Maximal Square
https://leetcode.com/problems/maximal-square/

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        self.matrix = matrix
        maxSize = 0
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                size = self.goDownRight(x, y)
                maxSize = max(maxSize, size)
        return maxSize ** 2
    def goDownRight(self, x, y):
        maxSize = min(len(self.matrix) - y, len(self.matrix[0]) - x)
        for size in range(1, maxSize+1):
            for j in range(y, y+size):
                for i in range(x, x+size):
                    if self.matrix[j][i] == "0":
                        return size-1
        return maxSize
