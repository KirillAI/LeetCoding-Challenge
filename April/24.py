'''
LRU Cache
https://leetcode.com/problems/lru-cache/

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        
    def removeFirst(self):
        self.head = self.head.next
        
    def removeLast(self):
        self.tail = self.tail.prev
        
    def remove(self, node):
        if node is self.head:
            self.removeFirst()
        elif node is self.tail:
            self.removeLast()
        else:
            prev = node.prev
            next = node.next
            node = None
            prev.next, next.prev = next, prev
        
    def addLast(self, node):
        if self.tail:
            self.tail.next, node.prev = node, self.tail
        if not self.head:
            self.head = node
        self.tail = node
        
class LRUCache:
    def __init__(self, capacity: int):
        self.lastAge = 0
        self.maxCap = capacity
        self.curCap = 0
        self.table = {}
        self.dll = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key in self.table:
            val = self.table[key].data
            self.put(key, val)
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            node = self.table[key]
            node.data = value
            self.dll.remove(node)
        else:
            node = Node(key, value)
            if self.curCap == self.maxCap:
                keyFirst = self.dll.head.key
                self.dll.removeFirst()
                del self.table[keyFirst]
            else:
                self.curCap += 1
        self.dll.addLast(node)
        self.table[key] = node
        self.lastAge += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
