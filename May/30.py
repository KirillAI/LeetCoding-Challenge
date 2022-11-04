'''
K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)

Note:

    1 <= K <= points.length <= 10000
    -10000 < points[i][0] < 10000
    -10000 < points[i][1] < 10000
'''

#**********************************
#*********** VERSION 1 ************
#**********************************
#Timsort

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda point: point[0]**2 + point[1]**2)[:K]

#**********************************
#*********** VERSION 2 ************
#**********************************
#Heapsort

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        import heapq
        return heapq.nsmallest(K, points, key=lambda point: point[0]**2 + point[1]**2)

#**********************************
#*********** VERSION 3 ************
#**********************************
#Divide and Conquer

class Solution(object):
    def kClosest(self, points, K):
        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def sort(i, j, K):
            # Partially sorts A[i:j+1] so the first K elements are
            # the smallest K elements.
            if i >= j: return

            # Put random element as A[i] - this is the pivot
            k = random.randint(i, j)
            points[i], points[k] = points[k], points[i]

            mid = partition(i, j)
            if K < mid - i + 1:
                sort(i, mid - 1, K)
            elif K > mid - i + 1:
                sort(mid + 1, j, K - (mid - i + 1))

        def partition(i, j):
            # Partition by pivot A[i], returning an index mid
            # such that A[i] <= A[mid] <= A[j] for i < mid < j.
            oi = i
            pivot = dist(i)
            i += 1

            while True:
                while i < j and dist(i) < pivot:
                    i += 1
                while i <= j and dist(j) >= pivot:
                    j -= 1
                if i >= j: break
                points[i], points[j] = points[j], points[i]

            points[oi], points[j] = points[j], points[oi]
            return j

        sort(0, len(points) - 1, K)
        return points[:K]
