# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        visited = deque([(root, 1)])

        while len(visited) != 0:
            curr, cnt = visited.popleft()
            if not curr:
                continue

            if not curr.left and not curr.right:
                return cnt

            visited.append([curr.left, cnt+1])
            visited.append([curr.right, cnt+1])
        return 0 

