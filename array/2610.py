class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        while len(nums) > 0 :
            s = set(nums)
            res.append(s)
            for num in s:
                nums.remove(num)
        return res