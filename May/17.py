'''
Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        pDic = Counter(p)
        aDic = Counter(s[:len(p)])
        pStart = 0
        pEnd = len(p)
        res = []
        if pDic == aDic:
            res.append(pStart)
        for pEnd in range(len(p), len(s)):
            aDic[s[pStart]] -= 1
            if aDic[s[pStart]] == 0:
                del aDic[s[pStart]]
            pStart += 1
            aDic[s[pEnd]] += 1
            if pDic == aDic:
                res.append(pStart)
        return res

#**********************************
#*********** VERSION 2 ************
#**********************************

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        pDic = Counter(p)
        aDic = Counter(s[:len(p)])
        aSet = set()
        for key in aDic:
            if aDic[key] == pDic[key]:
                aSet |= {key}
        pSet = set(pDic.keys())
        pStart = 0
        pEnd = len(p)
        res = []
        if aSet == pSet:
            res.append(pStart)
        for pEnd in range(len(p), len(s)):
            aDic[s[pStart]] -= 1
            if aDic[s[pStart]] > 0 and aDic[s[pStart]] == pDic[s[pStart]]:
                aSet |= {s[pStart]}
            else:
                aSet -= {s[pStart]}
            pStart += 1
            aDic[s[pEnd]] += 1
            if aDic[s[pEnd]] == pDic[s[pEnd]]:
                aSet |= {s[pEnd]}
            if aSet == pSet:
                res.append(pStart)
        return res

#**********************************
#*********** VERSION 3 ************
#**********************************

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        pLen = len(p)
        sLen = len(s)
        pHash = sHash = 0
        letterMap = {}
        if sLen < pLen:
            return []
        for i in range(ord('a'), ord('z') + 1):
            letterMap[chr(i)] = 2 ** (i - ord('a'))
        for i in range(pLen):
            sHash, pHash = sHash + letterMap[s[i]], pHash + letterMap[p[i]]
        if sHash == pHash:
            res.append(0)
        for i in range(pLen, sLen):
            sHash += letterMap[s[i]] - letterMap[s[i-pLen]]
            if sHash == pHash:
                res.append(i-pLen+1)
        return res
