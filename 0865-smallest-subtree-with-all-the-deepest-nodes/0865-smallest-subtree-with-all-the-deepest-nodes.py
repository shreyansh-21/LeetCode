from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        depth = {}
        
        # Step 1: DFS to compute depth of each node
        def dfs(node: Optional[TreeNode], d: int):
            if not node:
                return
            depth[node] = d
            dfs(node.left, d + 1)
            dfs(node.right, d + 1)
        
        dfs(root, 0)
        
        # Step 2: Find maximum depth
        max_depth = max(depth.values())
        
        # Step 3: Collect all deepest nodes
        deepest_nodes = [node for node, d in depth.items() if d == max_depth]
        
        # Step 4: LCA for binary tree
        def lca(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
            if not root or root == p or root == q:
                return root
            
            left = lca(root.left, p, q)
            right = lca(root.right, p, q)
            
            if left and right:
                return root
            return left or right
        
        # Step 5: Reduce LCA over all deepest nodes
        ans = deepest_nodes[0]
        for node in deepest_nodes[1:]:
            ans = lca(root, ans, node)
        
        return ans
