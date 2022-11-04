'''
Counting Elements
https://leetcode.com/problems/counting-elements/

#Subscribe to unlock.
'''

class Solution:
    def countElements(self, arr: List[int]) -> int:
        d = {}
        res = 0
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        keys = list(sorted(d.keys()))
        for i in range(1, len(keys)):
            if keys[i] - keys[i-1] == 1:
                res += d[keys[i-1]]
        return res
