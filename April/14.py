'''
Perform String Shifts
https://leetcode.com/problems/perform-string-shifts/

#Subscribe to unlock.
'''

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total = 0
        for i in range(len(shift)):
            total += shift[i][1] if shift[i][0] == 0 else -shift[i][1]
        if total > len(s) or -total>len(s):
            total = total % len(s)
        if total < 0:
            total = len(s) + total
        return s[total:] + s[:total]
