class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        limit = len(candyType)//2
        candy = set(candyType)

        if len(candy) >= limit:
            return limit
        else:
            return len(candy)
