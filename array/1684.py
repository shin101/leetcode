class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        allowed = set(allowed)

        for word in words:
            if all(char in allowed for char in word):
                res+=1

        return res