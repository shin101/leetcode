class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        def negative(arr):
            idx = len(arr)
            start = 0
            end = len(arr)-1
            while start<=end:
                mid=(start+end)//2
                if arr[mid]>=0:
                    end = mid-1
                else:
                    start = mid+1
                    idx = mid
            if idx == len(arr):
                return 0
            return len(arr[:idx+1])
        
        def positive(arr):
            start = 0
            end = len(arr)-1
            idx = len(arr)
            while start<=end:
                mid=(start+end)//2
                if arr[mid]>0:
                    end = mid-1
                    idx = mid
                else:
                    start = mid+1
            return len(arr[idx:])


        return max(positive(nums),negative(nums))
        
