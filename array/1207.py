from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = defaultdict(int)
        for num in arr:
            hashmap[num] += 1
        return len(hashmap.values()) == len(set(hashmap.values()))
        