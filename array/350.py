class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        map1 = Counter(nums1)
        map2 = Counter(nums2)
        shorter = nums1 if len(nums1) < len(nums2) else nums2
        longer = map1 if len(map1) > len(map2) else map2
        for num in shorter:
            if num in longer and longer[num] > 0:
                res.append(num)
                longer[num] -= 1
        
        return res