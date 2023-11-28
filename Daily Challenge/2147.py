class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10**9 + 7
        seats = []
        for idx, num in enumerate(corridor):
            if num == "S":
                seats.append(idx)
        
        if len(seats) < 2 or len(seats)%2 == 1 :
            return 0
        res = 1
        i = 1

        while i < len(seats) - 1:
            res *= seats[i+1] - seats[i]
            i+=2
        return res%mod