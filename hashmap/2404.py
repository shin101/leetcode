class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        c = {}
        for n in nums:
            if n%2==0:
                c[n] = c.get(n, 0)+1
        sorted_c = sorted(c.items(), key=lambda x:(x[1],-x[0]), reverse=True)

        if sorted_c:return sorted_c[0][0]
        
        return -1