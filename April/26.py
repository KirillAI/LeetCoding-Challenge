'''
Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/

Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:

    1 <= text1.length <= 1000
    1 <= text2.length <= 1000
    The input strings consist of lowercase English characters only.
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    m[i][j] = m[i-1][j-1] + 1
                else:
                    m[i][j] = max(m[i-1][j], m[i][j-1])
        return m[-1][-1]

#**********************************
#*********** VERSION 2 ************
#**********************************

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = min(len(text1)+1, len(text2)+1)
        m = max(len(text1)+1, len(text2)+1)
        if len(text2) > len(text1):
            text2, text1 = text1, text2
        ar = [0]*n
        for i in range(1, m):
            prev = 0
            for j in range(1, n):
                temp = ar[j]
                if text1[i-1] == text2[j-1]:
                    ar[j] = prev + 1
                else:
                    ar[j] = max(ar[j-1], ar[j])
                prev = temp
        return ar[-1]
