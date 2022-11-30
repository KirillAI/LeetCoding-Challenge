'''
Add Binary
https://leetcode.com/problems/add-binary/
#Easy #Array #String

Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
 
Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''

'''
Time: O(N)
Memory: O(N)
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a = '0' * (len(b) - len(a)) + a
        else:
            b = '0' * (len(a) - len(b)) + b
        add = '0'
        res = ''
        for i in range(-1, -len(a) - 1, -1):
            if a[i] == '1' and b[i] == '1':
                res = add + res
                add = '1'
            elif a[i] == '1' or b[i] == '1':
                if add == '0':
                    res = '1' + res
                else:
                    res = '0' + res
                    add = '1'
            else:
                res = add + res
                add = '0'
        if add == '1':
            res = add + res
        return res