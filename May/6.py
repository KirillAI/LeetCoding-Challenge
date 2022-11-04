'''
Majority Element
https://leetcode.com/problems/majority-element/

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        d = Counter(nums)
        for key in d:
            if d[key] > len(nums) // 2:
                return key

#**********************************
#*********** VERSION 2 ************
#**********************************

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = None
        n = 0
        for num in nums:
            if n == 0:
                res = num
            n += 1 if num == res else -1
        return res
