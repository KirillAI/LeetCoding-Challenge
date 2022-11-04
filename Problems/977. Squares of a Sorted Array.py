'''
Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Note:

    1 <= A.length <= 10000
    -10000 <= A[i] <= 10000
    A is sorted in non-decreasing order.
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(map(lambda x: x**2, A))

#**********************************
#*********** VERSION 2 ************
#**********************************

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        p0, p1 = 0, len(A) - 1
        res = []
        while p0 <= p1:
            if A[p0] + A[p1] > 0:
                res.append(A[p1] ** 2)
                p1 -= 1
            else:
                res.append(A[p0] ** 2)
                p0 += 1
        return res[::-1]

#**********************************
#*********** VERSION 3 ************
#**********************************

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        p1 = 0
        res = []
        while p1 < len(A) and A[p1] < 0:
            p1 += 1
        p0 = p1 - 1
        while p0 >= 0 and p1 < len(A):
            if A[p1] + A[p0] > 0:
                res.append(A[p0] ** 2)
                p0 -= 1
            else:
                res.append(A[p1] ** 2)
                p1 += 1
        while p0 >= 0:
            res.append(A[p0] ** 2)
            p0 -= 1
        while p1 < len(A):
            res.append(A[p1] ** 2)
            p1 += 1
        return res
