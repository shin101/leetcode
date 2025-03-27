class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = [int(s) for s in s.split(" ") if s.isdigit()]
        return s == sorted(s) and len(s) == len(set(s))
