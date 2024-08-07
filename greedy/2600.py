class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = 0

        while k >0:
            if numOnes:
                numOnes -= 1
                res +=1 
            elif numZeros:
                numZeros-=1
            else:
                numNegOnes -=1
                res-=1
            
            k-=1
        


        return res 