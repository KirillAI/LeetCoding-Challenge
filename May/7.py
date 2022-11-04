'''
Cousins in Binary Tree
https://leetcode.com/problems/cousins-in-binary-tree/

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:

Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

Note:

    The number of nodes in the tree will be between 2 and 100.
    Each node has a unique integer value from 1 to 100.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.height0 = None
        self.parent0 = None
        self.x = x
        self.y = y
        return self.dfs(root, root, 0)
    def dfs(self, parent, node, height):
        if not node:
            return False
        if node.val == self.x or node.val == self.y:
            if self.height0:
                return self.height0 == height and self.parent0.val != parent.val
            else:
                self.height0 = height
                self.parent0 = parent
        left = self.dfs(node, node.left, height+1)
        right = self.dfs(node, node.right, height+1)
        return left or right
