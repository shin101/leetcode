class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s)-1
        vowel = ["a", "e", "i", "o", "u","A","E","I","O","U"]
        s = list(s)

        while l < r :
            if s[l] in vowel:
                if s[r] in vowel:
                    s[l],s[r] = s[r], s[l]
                    l+=1
                r-=1
            else:
                l+=1
        return "".join(s)