'''
Uncrossed Lines
https://leetcode.com/problems/uncrossed-lines/

We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

    A[i] == B[j];
    The line we draw does not intersect any other connecting (non-horizontal) line.

Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.

Example 1:

Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.

Example 2:

Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3

Example 3:

Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2

Note:

    1 <= A.length <= 500
    1 <= B.length <= 500
    1 <= A[i], B[i] <= 2000
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        import collections
        matrix, m, n = collections.defaultdict(int), len(A), len(B)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                matrix[i, j] = max(matrix[i - 1, j - 1] + (A[i - 1] == B[j - 1]), matrix[i - 1, j], matrix[i, j - 1])
        return matrix[m, n]

#**********************************
#*********** VERSION 2 ************
#**********************************

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        lenA = len(A)
        lenB = len(B)
        matrix = []
        for i in range(lenB + 1):
            matrix.append([0] * (lenA + 1))
        for i in range(1, lenA + 1):
            for j in range(1, lenB + 1):
                matrix[j][i] = max(matrix[j - 1][i - 1] + (A[i - 1] == B[j - 1]), matrix[j - 1][i], matrix[j][i - 1])
        return matrix[-1][-1]

#**********************************
#*********** VERSION 3 ************
#**********************************

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        lenA = len(A)
        lenB = len(B)
        matrix = [0] * (lenB + 1)
        for i in range(lenA):
            for j in range(lenB)[::-1]:
                if A[i] == B[j]:
                    matrix[j + 1] = matrix[j] + 1
            for j in range(lenB):
                matrix[j + 1] = max(matrix[j + 1], matrix[j])
        return matrix[-1]

#**********************************
#*********** VERSION 4 ************
#**********************************

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        s = set(A) & set(B)
        A = [a for a in A if a in s]
        B = [b for b in B if b in s]
        lenA = len(A)
        lenB = len(B)
        matrix = [0] * (lenB + 1)
        for i in range(lenA):
            for j in range(lenB)[::-1]:
                if A[i] == B[j]:
                    matrix[j + 1] = matrix[j] + 1
            for j in range(lenB):
                matrix[j + 1] = max(matrix[j + 1], matrix[j])
        return matrix[-1]
