class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num = list(num)
        i = len(num)-1

        while num[i]=='0':
            num.pop()
            i-=1
        
        return "".join(num)