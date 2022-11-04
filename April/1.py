'''
Single Number
https://leetcode.com/problems/single-number/

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        res = nums[0]
        nums = sorted(nums)
        for i in range(len(nums)):
            if i == 0 and nums[i] != nums[i+1] or i == len(nums) - 1 and nums[i] != nums[i-1] or nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                res = nums[i]
        return res
