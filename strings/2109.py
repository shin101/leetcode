class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        s = list(s)
        j = 0
        
        for i, letter in enumerate(s):
            if j<len(spaces) and i == spaces[j]:
                res+=" "
                res += s[i]
                j+=1
            else:
                res += s[i]

        return res