# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        output = []
        if not root: return []

        while q:
            max_val = float("-inf")
            for i in range(len(q)):
                curr = q.popleft()
                max_val = max(max_val, curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            output.append(max_val)
        return output
