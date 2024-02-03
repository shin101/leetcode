class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        string = "123456789"
        l = r = 0 
        curr = ""
        res = []
        while l<len(string):
            if r<len(string):
                if  low <= int(string[l:r+1]) <= high:
                    res.append(int(string[l:r+1]))
                r+=1
            else:
                l+=1
                r=l
        
        res.sort()
        return res

