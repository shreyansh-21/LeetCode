# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, root):
        nodes = []  # store (col, row, val)
        
        def dfs(node, row, col):
            if not node:
                return
            nodes.append((col, row, node.val))
            dfs(node.left, row+1, col-1)
            dfs(node.right, row+1, col+1)
        
        dfs(root, 0, 0)

        # sort by col, then row, then value
        nodes.sort(key=lambda x: (x[0], x[1], x[2]))
        
        res = defaultdict(list)
        for col, row, val in nodes:
            res[col].append(val)
        
        return [res[x] for x in sorted(res)]
        
        