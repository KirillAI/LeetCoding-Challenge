'''
Remove Duplicates from Sorted Array II
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.

Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        _length = len(nums)
        p0 = 1
        p1 = 1
        while p1 < len(nums):
            if nums[p1] == nums[p1-1]:
                count += 1
            else:
                count = 0
            if count == 2:
                while p1 < len(nums) and nums[p1] == nums[p1-1]:
                    p1 += 1
                    _length -= 1
                count = 0
            if p1 == len(nums):
                break
            nums[p0] = nums[p1]
            p0 += 1
            p1 += 1
        return _length

#**********************************
#*********** VERSION 2 ************
#**********************************

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = min(2, len(nums))
        for num in nums[2:]:
            if num > nums[i-2]:
                nums[i] = num
                i += 1
        return i
