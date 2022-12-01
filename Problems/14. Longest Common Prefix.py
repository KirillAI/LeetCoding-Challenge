'''
Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/
#Array #Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

'''
Time: O(N^2)
Memory: O(1)
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        minLen = float('inf')
        for s in strs:
            minLen = min(minLen, len(s))
        if minLen == 0:
            return ''
        for i in range(minLen):
            t = strs[0][i]
            for s in strs[1:]:
                if s[i] != t:
                    return s[:i]
        return strs[0][:minLen]

#**********************************
#*********** VERSION 2 ************
#**********************************

'''
Time: O(N^2)
Memory: O(N)
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        nLetters = ord('z') - ord('a') + 1
        def getCode(s):
            #every letter is a number (nLetters bits), and word is a number with length * nLetters bits
            code = 0
            for c in s[::-1]:
                code <<= nLetters #shift the last letter
                code += 1 << (ord(c) - ord('a')) #letter is a bit position
            return code
        
        def decode(code):
            prefix = ''
            magic = (2 ** nLetters) - 1 # 111...11 - nLetters times
            decodeTable = {}
            for i in range(nLetters):
                decodeTable[1 << i] = chr(i + ord('a'))
            while code & magic != 0:
                prefix += decodeTable[code & magic] #get the last nLetters bits
                code >>= nLetters #delete the first code of symbol
            return prefix
        
        codes = list(map(getCode, strs))
        prefixCode = codes[0]
        for code in codes[1:]:
            prefixCode &= code
        prefix = decode(prefixCode)
        return prefix