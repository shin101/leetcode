class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        boundary = int(sqrt(c)) # 2
        for a in range(boundary+1):
            b = sqrt(c - a**2 )
            if b == int(b):
                return True

        return False

