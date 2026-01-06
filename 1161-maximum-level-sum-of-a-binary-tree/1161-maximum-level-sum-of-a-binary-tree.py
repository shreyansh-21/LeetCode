# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return None
        
        queue = deque()
        queue.append(root)
        answer =float('-inf')
        levels =1
        levelans =0

        while queue:
            level =[]
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            a = sum(level)
            if answer < a:
                answer = a
                levelans = levels
            levels = levels + 1

        return levelans
        