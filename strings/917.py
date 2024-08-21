class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        l = 0
        r = len(s)-1

        while l<r:
            if s[l].isalpha() and s[r].isalpha():
                s[l], s[r] = s[r], s[l]
                l+=1
                r-=1
            elif s[l].isalpha() and not s[r].isalpha():
                r-=1
            elif not s[l].isalpha() and s[r].isalpha():
                l+=1
            else:
                l+=1
                r-=1

        return "".join(s)

