class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        target = n/4

        for i in [arr[n//4], arr[n//2], arr[3*n//4]]:
            left = bisect_left(arr, i)
            right = bisect_right(arr, i) - 1
            if (right-left+1) > target:
                return i
        
        return -1

