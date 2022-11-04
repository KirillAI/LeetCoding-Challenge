'''
Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true

Note:

    You may assume that all inputs are consist of lowercase letters a-z.
    All inputs are guaranteed to be non-empty strings.
'''

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        found, cur, i = self.findSubstr(word)
        for j in range(i, len(word)):
            c = word[j]
            cur[c] = {}
            cur = cur[c]
        cur['END'] = 0
            

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        found, cur, i = self.findSubstr(word)
        return found and 'END' in cur

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        found, cur, i = self.findSubstr(prefix)
        return found
    
    def findSubstr(self, word):
        cur = self.head
        i = 0
        found = True
        while i < len(word):
            c = word[i]
            if c in cur:
                cur = cur[c]
            else:
                found = False
                break
            i += 1
        return found, cur, i


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
