# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        output = 0
        
        def dfs(node, max_sofar):
            nonlocal output 

            if not node:
                return 

            if node.val >= max_sofar:
                output += 1
                max_sofar = node.val
            
            dfs(node.left, max_sofar)
            dfs(node.right, max_sofar)

        dfs(root, root.val)
        return output