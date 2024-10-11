class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1] * len(arr)
        curr_max = 0

        for i in range(len(arr)-2, -1, -1):
            curr_max = max(curr_max, arr[i+1])
            res[i] = curr_max

        return res