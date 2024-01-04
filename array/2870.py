class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        print(c)
        res = 0

        for k,v in c.items():
            if v==1:
                return -1
            res += ceil(v/3)

        return res