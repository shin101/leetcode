class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = 0
        nums2 = [n*k for n in nums2]
        smallest_nums2 = min(nums2) #6

        for num in nums1:
            if num < smallest_nums2:
                continue
            for n in nums2:
                if num%n == 0:
                    res +=1


        return res