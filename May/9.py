'''
Valid Perfect Square
https://leetcode.com/problems/valid-perfect-square/

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true

Example 2:

Input: 14
Output: false
'''

#**********************************
#*********** VERSION 1 ************
#**********************************
#Binary Search

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 0
        high =  2 * num
        while low < high:
            mid = low + (high - low) // 2
            sqr = mid ** 2
            if sqr > num:
                high = mid
            elif sqr < num:
                low = mid + 1
            else:
                return True
        return False

#**********************************
#*********** VERSION 2 ************
#**********************************
#Newton's Method

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r = num
        while r * r > num:
            r = (r + num / r) // 2
        return r * r == num
