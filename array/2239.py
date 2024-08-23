class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        minus = float('-inf')
        plus = float('inf')

        for num in nums:
            if num ==0:
                return 0
            elif num < 0 and num > minus:
                minus = num
            elif num > 0 and num < plus:
                plus = num
        
        if abs(minus) == abs(plus):
            return plus
        elif abs(minus) < abs(plus):
            return minus
        
        return plus