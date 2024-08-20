class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        res = ['_'] * len(s)
        for word in s:
            res[int(word[-1])-1] = word[0:-1]
        
        return " ".join(res)