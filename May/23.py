'''
Interval List Intersections
https://leetcode.com/problems/interval-list-intersections/

Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

Example 1:

Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.

Note:

    0 <= A.length < 1000
    0 <= B.length < 1000
    0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        low = 0
        high = len(A)
        res = []
        newLow = low
        for b in B:  
            wasInter = False
            for i in range(low, high):
                a = A[i]
                bInA = a[0] <= b[0] <= a[1]
                aInB = b[0] <= a[0] <= b[1]
                if bInA or aInB:
                    newLow = i if not wasInter else newLow
                    wasInter = True
                    if bInA:
                        res.append(self.getIntersection(a, b))
                    else:
                        res.append(self.getIntersection(b, a))
                else:
                    if wasInter:
                        low = newLow
                        break
        return res
    def getIntersection(self, a, b):
        return [b[0], min(a[1], b[1])]

#**********************************
#*********** VERSION 2 ************
#**********************************

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = []
        while i < len(A) and j < len(B):
            a = A[i]
            b = B[j]
            low = max(a[0], b[0])
            high = min(a[1], b[1])
            if low <= high:
                res.append([low, high])
            if a[1] < b[1]:
                i += 1
            elif a[1] == b[1]:
                i += 1
                j += 1
            else:
                j += 1
        return res
