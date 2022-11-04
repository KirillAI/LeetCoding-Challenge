'''
Leftmost Column with at Least a One
https://leetcode.com/problems/leftmost-column-with-at-least-a-one/

#Subscribe to unlock.
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        left, right = 0, cols - 1
        setRows = set(range(rows))
        idxOne = 101
        while left <= right:
            mid = left + (right - left) // 2
            isOne = False
            delRows = []
            for row in setRows:
                val = binaryMatrix.get(row, mid)
                isOne |= val == 1
                if val == 0:
                    delRows.append(row)
            if isOne:
                setRows -= set(delRows)
                idxOne = min(idxOne, mid)
                right = mid - 1
            else:
                left = mid + 1
        return -1 if idxOne > 100 else idxOne

#**********************************
#*********** VERSION 2 ************
#**********************************

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        left, right = 0, cols - 1
        listRows = list(range(rows))
        idxOne = 101
        maxRows = rows - 1
        while left <= right:
            mid = left + (right - left) // 2
            isOne = False
            tmpMaxRows = maxRows
            i = 0
            while i <= tmpMaxRows:
                row = listRows[i]
                val = binaryMatrix.get(row, mid)
                isOne |= val == 1
                if val == 0:
                    listRows[i], listRows[tmpMaxRows] = listRows[tmpMaxRows], listRows[i]
                    tmpMaxRows -= 1
                else:
                    i += 1
            if isOne:
                maxRows = tmpMaxRows
                idxOne = min(idxOne, mid)
                right = mid - 1
            else:
                left = mid + 1
        return -1 if idxOne > 100 else idxOne

#**********************************
#*********** VERSION 3 ************
#**********************************

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        res = -1
        row, col = 0, cols - 1
        while row < rows and col >= 0:
            if binaryMatrix.get(row, col) == 1:
                res = col
                col -= 1
            else:
                row += 1
        return res

#**********************************
#*********** VERSION 4 ************
#**********************************

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        left, right = 0, cols - 1
        idxOne = 101
        while left <= right:
            mid = left + (right - left) // 2
            isOne = False
            for row in range(rows):
                val = binaryMatrix.get(row, mid)
                isOne |= val == 1
            if isOne:
                idxOne = min(idxOne, mid)
                right = mid - 1
            else:
                left = mid + 1
        return -1 if idxOne > 100 else idxOne
