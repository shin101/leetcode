class Solution:
    def findComplement(self, num: int) -> int:
        num = list(bin(num)[2:])

        for i in range(len(num)):
            if num[i] == "1":
                num[i] = "0"
            else:
                num[i] = "1"
        
        
        return (int(''.join(num),2))
        