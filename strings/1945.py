class Solution:
    def getLucky(self, s: str, k: int) -> int:
        temp = ""

        for char in s:
            temp += str(ord(char)-ord("a")+1)
        
        print(temp) #9999

        while k > 0:
            total = 0
            for num in temp:
                total += int(num)
            temp = str(total)

            k-=1

        return int(temp)

