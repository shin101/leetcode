# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        curr = 0 

        def inorder(node):
            nonlocal curr
            if not node:
                return

            inorder(node.right)
            curr += node.val 
            node.val = curr
            inorder(node.left)
        inorder(root)
        return root