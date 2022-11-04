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
        table = {0: -1}
        count = res = 0
        for i in range(len(nums)):
            count += 2 * nums[i] - 1
            if count in table:
                res = max(res, i - table[count])
            else:
                table[count] = i
        return res

#**********************************
#*********** VERSION 2 ************
#**********************************

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        table = {0: -1}
        count = res = 0
        for i, num in enumerate(nums):
            count += 1 if num == 0 else -1
            if count in table:
                res = max(res, i - table[count])
            else:
                table[count] = i
        return res
