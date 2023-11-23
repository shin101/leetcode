from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []

        def dfs(lst):
            diff = lst[1]-lst[0]
            for i in range(2, len(lst)):
                if lst[i]-lst[i-1] != diff:
                    return False
            return True
            

        for i, j in list(zip(l,r)):
            arr = nums[i:j+1]
            arr.sort()
            res.append(dfs(arr))

        return res