# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def length(root, depth):
            if not root:
                return depth
            depth += 1
            depth_left = length(root.left, depth)
            depth_right = length(root.right, depth)
            return max(depth_left, depth_right)
        return length(root, 0)

        

        