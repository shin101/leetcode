class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = min2 = float(inf)
        for i in range(len(prices)):
            if prices[i] < min1:
                min2 = min1
                min1 = prices[i]
            else:
                min2 = min(min2, prices[i])
        return money-min1-min2 if min1+min2<=money else money
