# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def recursion(node, level):
            if not node:
                return
            
            # when visiting a new level for the first time
            if len(res) == level:
                res.append(node.val)

            # right first, then left (to capture rightmost view)
            recursion(node.right, level + 1)
            recursion(node.left, level + 1)
        
        recursion(root, 0)
        return res
