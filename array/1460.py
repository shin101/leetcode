class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        c = Counter(target)
        a = Counter(arr)

        return c == a