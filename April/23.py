'''
Bitwise AND of Numbers Range
https://leetcode.com/problems/bitwise-and-of-numbers-range/

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4

Example 2:

Input: [0,1]
Output: 0
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        bigBit = 31
        if m == n:
            return m
        while n >> bigBit == 0 and bigBit > 0:
            bigBit -= 1
        if m >> bigBit == 0:
            return 0
        bit = bigBit
        while m >> bit == n >> bit:
            bit -= 1
        return m >> (bit+1) << (bit+1)

#**********************************
#*********** VERSION 2 ************
#**********************************

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == n:
            return m
        bit = 31
        while m >> bit == n >> bit:
            bit -= 1
        return m >> (bit+1) << (bit+1)

#**********************************
#*********** VERSION 3 ************
#**********************************

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        bit = 0
        while m != n:
            m >>= 1
            n >>= 1
            bit += 1
        return m << bit
