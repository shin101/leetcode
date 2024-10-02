class Solution: 
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)
        hashmap = {}
        res = []
        rank = 1

        for i, num in enumerate(sorted_arr, 1):
            if num not in hashmap:
                hashmap[num] = rank
                rank+=1

        for idx, a in enumerate(arr):
            arr[idx] = hashmap[a]
        return arr
