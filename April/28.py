'''
First Unique Number
https://leetcode.com/problems/first-unique-number/

#Subscribe to unlock.
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

from collections import deque
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = deque()
        self.d = {}
        for value in nums:
            self.add(value)

    def showFirstUnique(self) -> int:
        return -1 if not self.q else self.q[0]

    def add(self, value: int) -> None:
        if value in self.d:
            if self.d[value]:
                self.d[value] = None
                self.q.remove(value)
        else:
            self.q.append(value)
            self.d[value] = 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

#**********************************
#*********** VERSION 2 ************
#**********************************

from collections import deque
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = deque()
        self.uniq = set()
        self.notUniq = set()
        for value in nums:
            self.add(value)

    def showFirstUnique(self) -> int:
        return -1 if not self.q else self.q[0]

    def add(self, value: int) -> None:
        if value in self.uniq:
            self.uniq.remove(value)
            self.notUniq.add(value)
            self.q.remove(value)
        elif value not in self.notUniq:
            self.uniq.add(value)
            self.q.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

#**********************************
#*********** VERSION 3 ************
#**********************************

from collections import Counter, deque
class FirstUnique:
    def __init__(self, nums: List[int]):
        self.c = Counter()
        self.d = deque()
        for num in nums:
            self.add(num)


    def showFirstUnique(self) -> int:
        return -1 if not self.d else self.d[0]

    def add(self, value: int) -> None:
        self.c[value] += 1
        if self.c[value] == 2:
            self.d.remove(value)
        elif self.c[value] == 1:
            self.d.append(value)
        
# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

#**********************************
#*********** VERSION 4 ************
#**********************************

from collections import Counter, deque
class FirstUnique:
    def __init__(self, nums: List[int]):
        self.c = Counter(nums)
        self.d = deque(nums)

    def showFirstUnique(self) -> int:
        while self.d:
            if self.c[self.d[0]] > 1:
                self.d.popleft()
            else:
                return self.d[0]
        return -1

    def add(self, value: int) -> None:
        self.c[value] += 1
        self.d.append(value)
        
# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
