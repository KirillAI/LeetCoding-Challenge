'''
Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max = -2**16
        self.dbs_lrn(root)
        return self.max
    def dbs_lrn(self, node):
        if not node:
            return 0
        left = max(0, self.dbs_lrn(node.left))
        right = max(0, self.dbs_lrn(node.right))
        self.max = max(self.max, node.val + left + right)
        return max(left, right) + node.val

#**********************************
#*********** VERSION 2 ************
#**********************************

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max = float("-inf")
        self.dbs_lrn(root)
        return self.max
    def dbs_lrn(self, node):
        if not node:
            return 0
        left = self.dbs_lrn(node.left)
        right = self.dbs_lrn(node.right)
        self.max = max(self.max, node.val + left + right)
        return max(0, max(left, right) + node.val)
