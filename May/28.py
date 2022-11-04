'''
Counting Bits
https://leetcode.com/problems/counting-bits/

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]

Example 2:

Input: 5
Output: [0,1,1,2,1,2]

Follow up:

    It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
    Space complexity should be O(n).
    Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        pos = 0
        maxPos = 1
        for i in range(1, num + 1):
            res.append(res[pos] + 1)
            pos += 1
            if pos == maxPos:
                pos = 0
                maxPos = i + 1
        return res

#**********************************
#*********** VERSION 2 ************
#**********************************

class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        for i in range(1, num + 1):
            res.append(res[i & (i - 1)] + 1)
        return res

#**********************************
#*********** VERSION 3 ************
#**********************************

class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        for i in range(1, num + 1):
            res.append(res[i >> 1] + (i & 1))
        return res
