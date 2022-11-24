'''
Delete and Earn
https://leetcode.com/problems/delete-and-earn/
#DynamicProgramming #Medium

You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

Example 1:
Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.

Example 2:
Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.

Constraints:
1 <= nums.length <= 2 * 10^4
1 <= nums[i] <= 10^4
'''

'''
I will use dynamic programming. To do this, at each step I will choose what gives more points, based on the previous optimal solutions.

At each step, you have to decide what gives more points: the current number of points plus the points in the before previous step or the points in the previous step. The problem of finding the optimal solution is choosing value from minimum to maximum. To do this, I made two versions of the solution.

In the first version, I use two hash tables with sizes equal to the number of unique values in nums, but the unique values in nums are sorted.

In the second version of the solution, there is no sorting, but the size of the second hash table is equal to the maximum value in nums to ensure that values from nums is chosen consistently from minimum to maximum.

In practice, the first version will be more optimal if the number of unique values in nums is small and the values of nums are also small.
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

'''
Time: O(N log N)
Memory: O(N)
'''

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = {}
        opt = {}
        keys = []
        for num in nums:
            if num not in count:
                count[num] = 0
                keys.append(num)
            count[num] += 1
        keys = sorted(keys)
        opt[keys[0]] =  keys[0] * count[keys[0]]
        for i in range(1, len(keys)):
            key = keys[i]
            opt0 = opt[key - 1] if (key - 1) in opt else 0
            opt1 = key * count[key]
            if keys[i - 1] != key - 1:
                opt1 += opt[keys[i - 1]]
            elif i > 1 and keys[i - 2] != key - 1:
                opt1 += opt[keys[i - 2]]
            opt[key] = max(opt0, opt1)
        return opt[keys[-1]]

#**********************************
#*********** VERSION 2 ************
#**********************************

'''
Time: O(N)
Memory: O(max val in nums)
'''

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = {}
        opt = {}
        maxKey = 0
        for num in nums:
            if num not in count:
                count[num] = 0
                maxKey = max(maxKey, num)
            count[num] += 1
        opt[0] = 0
        opt[1] = count[1] if 1 in count else 0
        for key in range(2, maxKey + 1):
            opt0 = opt[key - 1]
            opt1 = key * count[key] if key in count else 0
            opt1 += opt[key - 2]
            opt[key] = max(opt0, opt1)
        return opt[maxKey]