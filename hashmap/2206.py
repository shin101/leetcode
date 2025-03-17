class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n = len(nums)//2
        c = Counter(nums)
        cnt = 0

        for k,v in c.items():
            if v%2!=0:
                return False
            else:
                cnt += v//2
                
        return True

    