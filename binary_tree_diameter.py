# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.answer = 0
        self.height(root)
        return self.answer
        
    def height(self, node):
        if node ==None: return 0
        left = self.height(node.left)
        right = self.height(node.right)
        self.answer = max(self.answer, left+right)
        return 1 + max(left,right)
