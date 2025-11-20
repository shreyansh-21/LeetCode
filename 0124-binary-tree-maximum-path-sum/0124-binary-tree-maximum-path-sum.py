# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')

        def solve(root):
            if root is None:
                return 0
            l = solve(root.left)
            r = solve(root.right)

            neeche_hi_milgaya_answer = l + r + root.val        # (1)
            koi_ek_acha = max(l, r) + root.val                 # (2)
            only_root_acha = root.val                          # (3)

            self.maxSum = max(self.maxSum,neeche_hi_milgaya_answer,
                              koi_ek_acha,only_root_acha)
            # return best downward path
            return max(koi_ek_acha, only_root_acha)

        solve(root)
        return self.maxSum

        