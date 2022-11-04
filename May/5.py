'''
First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters. 
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = float("inf")
        d = {}
        for idx, c in enumerate(s):
            if c not in d:
                d[c] = idx
            else:
                d[c] = float("inf")
        for key in d:
            res = min(res, d[key])
        return -1 if res == float("inf") else res

#**********************************
#*********** VERSION 2 ************
#**********************************

class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        d = Counter(s)
        for key in d:
            if d[key] == 1:
                return s.index(key)
        return -1
