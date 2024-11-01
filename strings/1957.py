class Solution:
    def makeFancyString(self, s: str) -> str:
        res=s[0]
        curr = s[0]
        cnt = 1

        for i in range(1,len(s)):
            if s[i] == curr and cnt <2:
                res+=s[i]
                cnt+=1
            elif s[i] == curr and cnt>=2:
                continue

            else:
                res+=s[i]
                curr =s[i]
                cnt = 1


        return res