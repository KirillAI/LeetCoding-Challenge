'''
N-th Tribonacci Number
https://leetcode.com/problems/n-th-tribonacci-number/
#DynamicProgramming #Easy

The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.


Example 1:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537
 
Constraints:
0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
'''

'''
We can write T[n] like this: T[n] = T[n-3] + T[n-2] + T[n-1]. And T[n+1] = T[n-2] + T[n-1] + T[n]. If we rewrite T[n+1] and use T[n] from the previous formula, we get: T[n+1] = (T[n-2] + T[n-1]) + T[n] = (T[n] - T[n-3]) + T[n] = 2 * T[n] - T[n-3].
For this implementation, we need constant memory: 4 values from T[n-3] to T[n].

Time: O(N)
Memory: O(1)
'''

class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1, 2]
        if n <= 3:
            return t[n]
        for i in range(4, n + 1):
            tLast = 2 * t[3] - t[0]
            for j in range(3):
                t[j] = t[j + 1]
            t[3] = tLast
        return t[3]