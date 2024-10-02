class Solution:
    def generateTheString(self, n: int) -> str:
        res = ""

        if n%2==0:
            while len(res) < n-1:
                res+= "a"
            res+="b"
        else:
            res = "a"*n

        return res