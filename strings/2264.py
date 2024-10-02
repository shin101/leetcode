class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        for i in range(len(num)-2):
            if len(set(num[i:i+3])) == 1:
                res = max(res,num[i:i+3])

        return res