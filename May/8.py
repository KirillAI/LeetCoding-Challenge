'''
Check If It Is a Straight Line
https://leetcode.com/problems/check-if-it-is-a-straight-line/

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Constraints:

    2 <= coordinates.length <= 1000
    coordinates[i].length == 2
    -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    coordinates contains no duplicate point.
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        k = self.getK(coordinates[0], coordinates[1]) 
        for i in range(2, len(coordinates)):
            if self.getK(coordinates[i-1], coordinates[i]) != k:
                return False
        return True
    def getK(self, coor0, coor1):
        dx = coor1[0] - coor0[0]
        dy = coor1[1] - coor0[1]
        if dx == 0:
            curK = float("inf")
        else:
            curK = dy / dx
        return curK

#**********************************
#*********** VERSION 2 ************
#**********************************

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        k = self.getK(coordinates[0], coordinates[1])
        b = coordinates[0][1] - k * coordinates[0][0]
        for i in range(2, len(coordinates)):
            if k * coordinates[i][0] + b != coordinates[i][1]:
                return False
        return True
    def getK(self, coor0, coor1):
        dx = coor1[0] - coor0[0]
        dy = coor1[1] - coor0[1]
        if dx == 0:
            curK = float("inf")
        else:
            curK = dy / dx
        return curK

#**********************************
#*********** VERSION 3 ************
#**********************************

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[:2]
        dx0, dy0 = x1 - x0, y1 - y0
        for x, y in coordinates[2:]:
            if dx0 * (y - y1) != (x - x1) * dy0:
                return False
        return True

#**********************************
#*********** VERSION 4 ************
#**********************************

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[:2]
        dx0, dy0 = x1 - x0, y1 - y0
        return all(dx0 * (y - y1) == (x - x1) * dy0 for x, y in coordinates[2:])
