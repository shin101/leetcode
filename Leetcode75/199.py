class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        output = []

        while q:
            right_most = len(q)-1
            for i in range(len(q)):
                node = q.popleft()
                if node and i == right_most:
                    output.append(node.val)
                if node and node.left:
                    q.append(node.left)
                if node and node.right:
                    q.append(node.right)


        return output
