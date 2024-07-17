class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bn = bin(n)[2:]

        for i in range(1,len(bn)):
            if bn[i-1] == bn[i]:
                return False
            
        return True
