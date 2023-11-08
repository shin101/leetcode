class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy and t==1:
            return False

        chev_dist = max(abs(fx-sx), abs(fy-sy))
        return chev_dist <= t
