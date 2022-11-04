'''
Binary Tree Maximum Path Sum
https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/

#Subscribe to unlock.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        self.arr = arr
        return self.dbs_nlr(root, 0)
    def dbs_nlr(self, node, nVal):
        if not node or nVal == len(self.arr) or node.val != self.arr[nVal]:
            return False
        if not node.left and not node.right and node.val == self.arr[nVal] and nVal == len(self.arr)-1:
            return True
        left = self.dbs_nlr(node.left, nVal+1)
        right = self.dbs_nlr(node.right, nVal+1)
        return left or right
