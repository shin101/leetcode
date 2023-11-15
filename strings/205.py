class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        zipped = (set(zip(s,t)))
        return len(zipped) == len(set(s)) == len(set(t))
