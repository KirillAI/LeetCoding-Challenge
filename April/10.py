'''
Min Stack
https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

class Node:
    def __init__(self, _data):
        self.data = _data
        self.next = None
        self._min = None

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None
        
    def push(self, x: int) -> None:
        if self.head is None:
            self.head = Node(x)
            self.head._min = x
        else:
            self.head, self.head.next = Node(x), self.head
            self.head._min = min(self.head.next._min, x)

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.data

    def getMin(self) -> int:
        return self.head._min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#**********************************
#*********** VERSION 2 ************
#**********************************

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = [None]
        self.i = 1
        self._min = [None]
        self.len = 1

    def push(self, x: int) -> None:
        if self.i == self.len:
            self.data.append(0)
            self._min.append(0)
            self.len += 1
        self.data[self.i] = x
        self._min[self.i] = min(self._min[self.i-1], x) if self.i > 1 else x
        self.i += 1

    def pop(self) -> None:
        self.i = max(1, self.i - 1)

    def top(self) -> int:
        return self.data[self.i-1]

    def getMin(self) -> int:
        return self._min[self.i-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#**********************************
#*********** VERSION 3 ************
#**********************************

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = [[None, None]]
        self.i = 1
        self.len = 1       

    def push(self, x: int) -> None:
        if self.i == self.len:
            self.data.append([0 ,0])
            self.len += 1
        self.data[self.i][0] = x
        self.data[self.i][1] = min(self.data[self.i-1][1], x) if self.i > 1 else x
        self.i += 1

    def pop(self) -> None:
        self.i = max(1, self.i - 1)

    def top(self) -> int:
        return self.data[self.i-1][0]

    def getMin(self) -> int:
        return self.data[self.i-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
