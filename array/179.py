class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)
        
        def myfunc(n1, n2):
            if n1+n2 > n2+n1:
                return -1
            else:
                return 1
        
        # nums = ['10', '2']

        nums = sorted(nums, key=cmp_to_key(myfunc))

        return str(int("".join(nums)))
