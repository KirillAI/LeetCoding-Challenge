
'''
Palindrome Partitioning
#DynamicProgramming #dfs #medium
https://leetcode.com/problems/palindrome-partitioning/

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.
'''

'''Let's split the input string into substrings and check it for palindrome.
We can represent the substring search as a tree, where nodes on the same level -
change the size of the substring, and nodes on different levels - shift the substring.

We will use depth-first search algorithm with stack. The stack consists of two parts for every node:
indexes start and end of substrings, and current palindromes of the node.
'''
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        #double stack to fix indexes of start and end of substrings and palindromes of the current node
        stack = [[{'indexes': (0, i), 'curRes': []} for i in range(len(s))]]
        while len(stack) > 0:
            d = stack[-1][0] #the first node of the current level
            indexes = d['indexes']
            curRes = [i for i in d['curRes']] #make copy
            start, end = indexes
            del stack[-1][0]
            if len(stack[-1]) == 0:
                #we checked all nodes for the current level
                del stack[-1]
            if s[start:end+1] == s[start:end+1][::-1]:
                curRes.append(s[start:end+1])
                if end + 1 < len(s):
                    #add new level for the current node
                    stack.append([{'indexes': (end + 1, i), 'curRes': curRes} for i in range(end + 1, len(s))])
                else:
                    #we checked full string s
                    res.append(curRes)
        return res

sol = Solution()
print(sol.partition('aab'))