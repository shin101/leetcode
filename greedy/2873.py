class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        highest_diff = 0
        highest = 0

        for num in nums:
            highest = max(highest, num) 
            res = max(highest_diff*num, res)
            highest_diff = max(highest-num, highest_diff)


        return res
