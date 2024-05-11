# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 0)])

        max_depth = 0
        output = 0
        
        while q:
            curr, depth = q.popleft()

            if depth > max_depth:
                max_depth = depth
                output = 0
            if depth == max_depth:
                output += curr.val

            if curr.left:
                q.append((curr.left, depth+1))
            if curr.right:
                q.append((curr.right, depth+1))

        return output


