class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        third = 1

        for i in range(len(n)-1,-1,-1):
            if third%3==0 and i!=0:
                n = n[:i] + "." + n[i:]
            third+=1
        
        return n