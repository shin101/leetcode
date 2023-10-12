# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:



# Find peak 
# binary search two more times to find whether the value occurs on either side of the peak

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        l = 1
        r = length - 2

        # find peak
        while l <= r :
            m = (l+r)//2
            left = mountain_arr.get(m-1)
            mid = mountain_arr.get(m)
            right = mountain_arr.get(m+1)
            if left < mid < right : 
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                break
        peak = m

        # search left
        l,r = 0, peak
        while l <= r :
            m = (l + r)//2
            mid = mountain_arr.get(m)
            if mid < target:
                l = m + 1
            elif mid > target:
                r = m -1 
            else:
                return m 

        # search right
        l, r = peak, length-1
        while l <= r :
            m = (l + r)//2
            mid = mountain_arr.get(m)
            if mid < target:
                r = m -1 
            elif mid > target:
                l = m + 1
            else:
                return m
        return -1 