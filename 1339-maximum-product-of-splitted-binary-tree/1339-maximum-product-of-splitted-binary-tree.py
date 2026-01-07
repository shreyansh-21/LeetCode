# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.totalSum = 0
        self.best = 0

    def sumdfs(self, root):
        if not root:
            return 0
        return root.val + self.sumdfs(root.left) + self.sumdfs(root.right)

    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        subSum = root.val + left + right
        remaining = self.totalSum - subSum

        self.best = max(self.best, subSum * remaining)

        return subSum

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7

        self.totalSum = self.sumdfs(root)
        self.dfs(root)

        return self.best % MOD

    
