class Solution:
    def findGCD(self, nums: List[int]) -> int:
        res = 0
        max_num = -float('inf')
        min_num = float('inf')


        for num in nums:
            if num>max_num:
                max_num=num
            if num<min_num:
                min_num = num
        
        for i in range(min_num, 0, -1):
            if max_num%i==0 and min_num%i==0:
                return i

