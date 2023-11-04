# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        r1_leaf_nodes = []
        r2_leaf_nodes = []

        def dfs(node, arr):
            if not node:
                return
            
            if not node.right and not node.left:
                arr.append(node.val)
        
            dfs(node.left, arr)
            dfs(node.right, arr)

        dfs(root1, r1_leaf_nodes)
        dfs(root2, r2_leaf_nodes)
        return r1_leaf_nodes == r2_leaf_nodes
