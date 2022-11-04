'''
Sort Characters By Frequency
https://leetcode.com/problems/sort-characters-by-frequency/

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        d = Counter(s)
        keys = sorted(d, key=d.get, reverse=True)
        s = ""
        for key in keys:
            s += key * d[key]
        return s

#**********************************
#*********** VERSION 2 ************
#**********************************

class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        d = Counter(s)
        s = ""
        for key, val in sorted(d.items(), key=lambda x: x[1], reverse=True):
            s += val * key
        return s

#**********************************
#*********** VERSION 3 ************
#**********************************

class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        d = Counter(s)
        mas = [[] for i in range(len(s)+1)]
        for key in d:
            mas[d[key]].append(key)
        s = ""
        for key in mas[::-1]:
            if key != []:
                for k in key:
                    s += d[k] * k
        return s
