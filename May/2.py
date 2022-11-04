'''
Jewels and Stones
https://leetcode.com/problems/jewels-and-stones/

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:

Input: J = "z", S = "ZZ"
Output: 0

Note:

    S and J will consist of letters and have length at most 50.
    The characters in J are distinct.
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        from collections import Counter
        d = Counter(S)
        res = 0
        for j in J:
            res += d[j]
        return res

#**********************************
#*********** VERSION 2 ************
#**********************************

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        from collections import Counter
        d = Counter(S)
        return sum(value if key in J else 0 for key, value in d.items())
