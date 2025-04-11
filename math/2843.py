class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0

        for i in range(low, high+1):
            i = str(i)
            if len(i)%2==0:
                mid = len(i)//2
                first_half = sum(int(num) for (num) in i[:mid])
                second_half = sum(int(num) for num in i[mid:])
                if first_half == second_half:
                    res+=1
        return res

