class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        print(piles)
        for i in range(len(piles)//3, len(piles)-1, 2):
            res += piles[i]
        return res