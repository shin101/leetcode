class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)):
        #     if nums[i] in nums[i+1:i+k+1]:
        #         return True
        # return False

        hashset = defaultdict(int)

        for i, num in enumerate(nums):
            if num in hashset and i-hashset[num] <= k:
                return True

            else:
                hashset[num] = i

            
        return False

