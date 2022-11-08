'''
Pascal's Triangle
#Dynamic Programming #Easy
https://leetcode.com/problems/pascals-triangle/submissions/

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

Constraints:
1 <= numRows <= 30
'''

'''
First, we will add base solutions for the first two rows.
And then by incrementing the row, we will reuse the previous solution by summation.
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows > 1:
            res.append([1, 1])
        if numRows > 2:
            for i in range(2, numRows):
                res.append([1])
                for j in range(1, i):
                    res[-1].append(res[-2][j-1]+res[-2][j])
                res[-1].append(1)
        return res