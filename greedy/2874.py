class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        biggest = 0
        max_diff = 0


        for num in nums:
            biggest = max(biggest, num) 
            res = max(res, max_diff*num) 
            max_diff = max(biggest-num, max_diff) 
        

        return res



