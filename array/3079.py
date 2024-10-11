class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            biggest = max(str(n))
            print(biggest)
            nums[i] = int((biggest)*len(str(n)))
        
        return(sum(nums))