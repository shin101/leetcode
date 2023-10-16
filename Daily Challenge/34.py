class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.search(nums, target, False)
        right = self.search(nums, target, True)
        
        return [left, right]

    def search(self, nums, target, rightBias):
        l = 0
        r = len(nums)-1
        i = -1
        
        while l <= r : 
            mid = (l+r)//2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else: 
                i = mid
                if rightBias:
                    l = mid + 1
                else:
                    r = mid - 1
            
        return i 



        # [5,7,7,8,8,8,8,8,8,8,8,10,11]