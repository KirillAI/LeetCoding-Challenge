'''
Contiguous Array
https://leetcode.com/problems/contiguous-array/

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: len(nums)}
        _sum = 0
        res = 0
        i = len(nums) - 1
        for num in nums[::-1]:
            _sum += 2 * num - 1
            if _sum not in d:
                d[_sum] = i
            i -= 1
        if _sum == 0:
            return len(nums)
        if _sum in d:
            res = d[_sum]
        for i, num in enumerate(nums):
            _sum -= 2 * num - 1
            if _sum in d:
                res = max(res, d[_sum] - i - 1)
        return res

#**********************************
#*********** VERSION 2 ************
#**********************************

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: -1}
        _sum = res = 0
        for i, num in enumerate(nums):
            _sum += 2 * num - 1
            if _sum in d:
                res = max(res, i - d[_sum])
            else:
                d[_sum] = i
        return res
