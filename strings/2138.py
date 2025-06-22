class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        if len(s)%k==0:
            return [s[i:i+k] for i in range(0,len(s),k)]
        else:
            res = [s[i:i+k] for i in range(0,len(s),k)]
            while len(res[-1])!=k:
                res[-1]+=fill
            return res
            