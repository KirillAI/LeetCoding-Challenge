'''
Single Element in a Sorted Array
https://leetcode.com/problems/single-element-in-a-sorted-array/

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10

Note: Your solution should run in O(log n) time and O(1) space.
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if mid < len(nums) - 1:
                firstNum = nums[mid] == nums[mid + 1]
            else:
                firstNum = nums[mid] != nums[mid - 1]
            halfEven = (mid - low) % 2 == 0
            if not(firstNum) and halfEven or firstNum and not(halfEven):
                high = mid
            else:
                low = mid + 1
                if halfEven:
                    low += 1
        return nums[low]

#**********************************
#*********** VERSION 2 ************
#**********************************

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] != nums[mid + 1]:
                high = mid
            else:
                low = mid + 2
        return nums[low]
