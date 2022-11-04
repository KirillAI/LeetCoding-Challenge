'''
Ransom Note
https://leetcode.com/problems/ransom-note/

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)
        p0 = p1 = 0
        while p0 < len(ransomNote) and p1 < len(magazine):
            if ransomNote[p0] == magazine[p1]:
                p0 += 1
                p1 += 1
            else:
                p1 += 1
        return p0 == len(ransomNote)

#**********************************
#*********** VERSION 2 ************
#**********************************

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        d0, d1 = Counter(ransomNote), Counter(magazine)
        for key in d0:
            if d1[key] < d0[key]:
                return False
        return True

#**********************************
#*********** VERSION 3 ************
#**********************************

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        d = Counter(magazine)
        for s in ransomNote:
            if d[s] == 0:
                return False
            d[s] -= 1
        return True
