class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        new_set = set()

        for num in nums:
            if num>k:
                new_set.add(num)

        return len(new_set) if new_set else -1

