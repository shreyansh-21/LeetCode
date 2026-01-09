# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        
        if root ==p or root ==q:
            return root

        #finding left and right node
        leftn = self.lowestCommonAncestor(root.left,p,q)
        rightn = self.lowestCommonAncestor(root.right,p,q)

        if leftn is not None and rightn is not None:
            return root
        if leftn is not None:
            return leftn
        return rightn
        