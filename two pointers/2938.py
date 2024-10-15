class Solution:
    def minimumSteps(self, s: str) -> int:
        cnt_one = 0
        res = 0
        for i in range(len(s)):
            if s[i] == "1":
                cnt_one+=1
            else:
                res+=cnt_one
        
        return res