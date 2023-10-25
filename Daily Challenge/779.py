class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        l, r = 0, 2**(n-1)
        output = 0

        for i in range(n-1):
            mid = (l+r)//2
            
            if k <=mid:
                r = mid
            else:
                l = mid + 1
                output = 1 if not output else 0
        return output


