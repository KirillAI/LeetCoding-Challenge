'''
Edit Distance
https://leetcode.com/problems/edit-distance/

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5

Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
'''

#**********************************
#*********** VERSION 1 ************
#**********************************
#Dynamic programming

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == "" or word2 == "":
            return max(len(word1), len(word2))
        matrix = [[0] * (len(word1) + 1) for i in range(len(word2) + 1)]
        for i in range(len(word2) + 1):
            matrix[i][0] = i
        for j in range(len(word1) + 1):
            matrix[0][j] = j  
        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                if word1[j-1] == word2[i-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]) + 1
        return matrix[-1][-1]

#**********************************
#*********** VERSION 2 ************
#**********************************
#Dynamic programming, recursion

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i < 0 or j < 0:
                return max(i, j) + 1
            return dp(i-1, j-1) if word1[j] == word2[i] \
              else min(dp(i-1, j-1), dp(i-1, j), dp(i, j-1)) + 1
        return dp(len(word2) - 1, len(word1) - 1)
