'''
Maximum Sum Circular Subarray
https://leetcode.com/problems/maximum-sum-circular-subarray/

Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3

Example 2:

Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10

Example 3:

Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4

Example 4:

Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3

Example 5:

Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1

Note:
    -30000 <= A[i] <= 30000
    1 <= A.length <= 30000
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        minSum, maxSum = self.getMinMaxSum(A)
        #A[-2] + A[-1] + A[0] is sum(A) - sum(A[1:-3])
        max0 = sum(A) - minSum
        max1 = maxSum
        return max1 if max0 == 0 else max(max0, max1) #max0 = 0 if all a in A < 0
    def getMinMaxSum(self, A):
        minSum = tmpMinSum = maxSum = tmpMaxSum = A[0]
        for a in A[1:]:
            #searching for min sum
            curMinSum = tmpMinSum + a
            if curMinSum < 0 and curMinSum < a:
                tmpMinSum = curMinSum
            else:
                tmpMinSum = a
            minSum = min(minSum, tmpMinSum)
            #searching for max sum
            curMaxSum = tmpMaxSum + a
            if curMaxSum > 0 and curMaxSum > a:
                tmpMaxSum = curMaxSum
            else:
                tmpMaxSum = a
            maxSum = max(maxSum, tmpMaxSum)
        return minSum, maxSum

#**********************************
#*********** VERSION 2 ************
#**********************************
#The same but shorter

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        import operator
        minSum = self.getMinMaxSum(A, operator.lt)
        maxSum = self.getMinMaxSum(A, operator.gt)
        #A[-2] + A[-1] + A[0] is sum(A) - sum(A[1:-3])
        max0 = sum(A) - minSum
        max1 = maxSum
        return max1 if max0 == 0 else max(max0, max1) #max0 = 0 if all a in A < 0
    def getMinMaxSum(self, A, comparison_f):
        _sum = tmpSum = A[0]
        for a in A[1:]:
            curSum = tmpSum + a
            if comparison_f(curSum, 0) and comparison_f(curSum, a):
                tmpSum = curSum
            else:
                tmpSum = a
            _sum = _sum if comparison_f(_sum, tmpSum) else tmpSum
        return _sum

#**********************************
#*********** VERSION 3 ************
#**********************************

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        import operator
        #A[-2] + A[-1] + A[0] is sum(A) - sum(A[1:-3])
        max0 = sum(A) - self.getMinMaxSum(A, operator.lt)
        max1 = self.getMinMaxSum(A, operator.gt)
        return max1 if max0 == 0 else max(max0, max1) #max0 = 0 if all a in A < 0
    def getMinMaxSum(self, A, comparison_f):
        _sum = curSum = A[0]
        for a in A[1:]:
            curSum = a + (curSum if comparison_f(curSum, 0) else 0)
            _sum = _sum if comparison_f(_sum, curSum) else curSum
        return _sum
