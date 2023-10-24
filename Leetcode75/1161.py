# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        leveled = []
        max_sum = float(-inf)
        output = 0

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if level:
                leveled.append(level)

        print(leveled)
        for idx,arr in enumerate(leveled):
            if sum(arr) > max_sum:
                max_sum = sum(arr)
            # output is idx of where max sum is 
                output = idx+1

        return output