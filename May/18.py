'''
Permutation in String
https://leetcode.com/problems/permutation-in-string

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False

Note:

    The input strings only contain lower case letters.
    The length of both given strings is in range [1, 10,000].
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lenS1 = len(s1)
        lenS2 = len(s2)
        if lenS1 > lenS2:
            return False
        lettersHash = {}
        for c in range(ord('a'), ord('z')+1):
            lettersHash[chr(c)] = 2 ** (c - ord('a'))
        s1Hash = substrHash = 0
        for i in range(lenS1):
            s1Hash, substrHash = s1Hash + lettersHash[s1[i]], substrHash + lettersHash[s2[i]]
        if s1Hash == substrHash:
            return True
        for i in range(lenS1, lenS2):
            substrHash += lettersHash[s2[i]] - lettersHash[s2[i-lenS1]]
            if s1Hash == substrHash:
                return True
        return False
