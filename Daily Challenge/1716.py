class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        curr = 1
        day = 0

        while day < n : 
            res += curr
            curr += 1
            day += 1
            if day%7 == 0 :
                curr = day//7 + 1

        return res