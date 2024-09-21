class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        s = sorted(arr)
        diff = s[1] - s[0]
        for i in range(1, len(s)-1):
            if s[i+1] - s[i] != diff:
                return False
        

        return True