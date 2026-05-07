# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root :
            return True
        left_height = self.Depth(root.left)
        right_height = self.Depth(root.right)
        if abs(left_height - right_height) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
    
    def Depth(self, root):
        if not root:
            return 0
        return 1 + max(self.Depth(root.left), self.Depth(root.right))
        
