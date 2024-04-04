class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        curr = 0
        for letter in s:
            if letter == '(':
                curr += 1
            if letter == ')':
                curr -= 1
            res = max(res, curr)
        return res