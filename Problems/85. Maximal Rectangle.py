'''
Maximal Rectangle
https://leetcode.com/problems/maximal-rectangle/

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix[0])
        height = [0]*(m + 1)
        maxA = 0
        for row in matrix:
            for j in range(m):
                height[j] = (height[j] + 1 if row[j] == "1" else 0)
            stack = [-1]
            for j in range(m + 1):
                while height[j] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = j - 1 - stack[-1]
                    maxA = max(maxA, h * w)
                stack.append(j)
        return maxA

#**********************************
#*********** VERSION 2 ************
#**********************************

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        height = [0]*m
        left = [0]*m
        right = [m]*m
        maxA = 0
        for i in range(n):
            cur_left = 0
            cur_right = m
            for j in range(m):
                k = m - j - 1
                if matrix[i][j] == "1":
                    height[j] += 1
                    left[j] = max(cur_left, left[j])
                else:
                    height[j] = 0
                    left[j] = 0
                    cur_left = j + 1
                if matrix[i][k] == "1":
                    right[k] = min(cur_right, right[k])
                else:
                    right[k] = m
                    cur_right = k
            for j in range(m):
                maxA = max(maxA, height[j]*(right[j] - left[j]))
        return maxA
