'''
Move Zeroes
https://leetcode.com/problems/move-zeroes/

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = p1 = 0
        for p0 in range(len(nums)):
            p1 = max(p1, p0)
            while p1 < len(nums) and nums[p1] == 0:
                p1 += 1
            if p1 == len(nums):
                break
            if nums[p0] == 0:
                nums[p0], nums[p1] = nums[p1], nums[p0]
                p1 += 1
