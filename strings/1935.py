class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        hashset = set(brokenLetters)
        res = 0

        for t in text.split(" "):
            if (bool(hashset & set(t))) == False:
                res+=1

        return res