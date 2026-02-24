# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node: Optional[TreeNode], curr: int) -> int:
            if not node:
                return 0
            
            # Build the binary number
            curr = (curr << 1) | node.val
            if not node.left and not node.right:
                return curr
            
            # Sum of left and right subtree
            return dfs(node.left, curr) + dfs(node.right, curr)
        
        return dfs(root, 0)