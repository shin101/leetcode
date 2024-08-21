class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        r = len(nums)-1
        l = 0

        while l<r:
            if nums[l]%2!=0 and nums[r]%2==0:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
            elif nums[l]%2==0 and nums[r]%2==0:
                l+=1
            elif nums[l]%2== 0 and nums[r]!=1:
                l+=1
                r-=1
            else:
                r-=1
        
        return nums

