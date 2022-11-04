'''
Construct Binary Search Tree from Preorder Traversal
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Constraints:

    1 <= preorder.length <= 100
    1 <= preorder[i] <= 10^8
    The values of preorder are distinct.
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        head = None
        for node in preorder:
            if head is None:
                head = TreeNode(node)
            else:
                current = head
                while current is not None:
                    if node <= current.val:
                        if current.left is None:
                            current.left = TreeNode(node)
                            break
                        current = current.left
                    else:
                        if current.right is None:
                            current.right = TreeNode(node)
                            break
                        current = current.right
        return head

#**********************************
#*********** VERSION 2 ************
#**********************************

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    i = 0
    def bstFromPreorder(self, A, bound=float('inf')):
        if self.i == len(A) or A[self.i] > bound:
            return None
        root = TreeNode(A[self.i])
        self.i += 1
        root.left = self.bstFromPreorder(A, root.val)
        root.right = self.bstFromPreorder(A, bound)
        return root
