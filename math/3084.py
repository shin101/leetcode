class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        m = s.count(c)
        return floor(m * (m+1) / 2)
