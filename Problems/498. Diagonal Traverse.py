'''
Diagonal Traverse
https://leetcode.com/problems/diagonal-traverse/
#Array #Medium

Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-10^5 <= mat[i][j] <= 10^5
'''

'''
Time: O(N)
Memory: O(N)
'''

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        d = {}
        m = len(mat)
        n = len(mat[0])
        for y in range(m):
            for x in range(n):
                if x + y not in d:
                    d[x + y] = []
                d[x + y].append(mat[y][x])
        for xy in d:
            if xy %  2 == 0:
                res.extend(d[xy][::-1])
            else:
                res.extend(d[xy])
        return res