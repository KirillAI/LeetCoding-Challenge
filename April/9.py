'''
Backspace String Compare
https://leetcode.com/problems/backspace-string-compare/

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:

    1 <= S.length <= 200
    1 <= T.length <= 200
    S and T only contain lowercase letters and '#' characters.

Follow up:

    Can you solve it in O(N) time and O(1) space?
'''

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.getNewStr(S) == self.getNewStr(T)
    def getNewStr(self, _str):
        p = 0
        for i in range(len(_str)):
            if _str[i] == "#":
                p = max(-1, p - 2)
            else:
                _str = _str[:p] + _str[i] + _str[p+1:]
            p += 1
        return _str[:p]
