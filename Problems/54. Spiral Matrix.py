'''
Spiral Matrix
https://leetcode.com/problems/spiral-matrix/
#Array #Medium

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

'''
Time: O(N)
Memory: O(N)
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        mode = 0
        res = []
        while len(matrix) > 0:
            if mode % 4 == 0:
                res.extend(matrix.pop(0))
            elif mode % 4 == 1:
                res.extend([i.pop() for i in matrix])
            elif mode % 4 == 2:
                res.extend(matrix.pop(-1)[::-1])
            else:
                res.extend([i.pop(0) for i in matrix[::-1]])
            matrix = list(filter(lambda x: len(x) > 0, matrix))
            mode += 1
        return res

#**********************************
#*********** VERSION 2 ************
#**********************************

'''
Time: O(N)
Memory: O(N)
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        hMin = 0
        hMax = len(matrix)
        wMin = 0
        wMax = len(matrix[0])
        res = []
        mode = 0
        while len(res) < len(matrix) * len(matrix[0]):
            if mode % 4 == 0:
                res.extend(matrix[hMin][wMin:wMax])
                hMin += 1
            elif mode % 4 == 1:
                res.extend([i[wMax - 1] for i in matrix[hMin:hMax]])
                wMax -= 1
            elif mode % 4 == 2:
                res.extend(matrix[hMax - 1][wMin:wMax][::-1])
                hMax -= 1
            else:
                res.extend([i[wMin] for i in matrix[hMin:hMax][::-1]])
                wMin += 1
            mode += 1
        return res