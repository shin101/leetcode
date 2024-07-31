class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node, string): 
            nonlocal res

            if not node:
                return

            string += str(node.val)

            dfs(node.left, string)
            dfs(node.right, string)

            if not node.left and not node.right:
               res += int(string,2)

        dfs(root, "")
        return res
