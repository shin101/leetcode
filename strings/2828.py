class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        res = ''
        for w in words:
            res+=w[0]
        return res == s