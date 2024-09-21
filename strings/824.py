class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        res = []
        sentence = sentence.split(" ")
        print(sentence)

        for i, s in enumerate(sentence):
            if s[0].lower() in vowels:
                res.append (s+"ma"+("a"*(i+1)))
            else:
                modified = (s[1:] + s[0]+"ma"+("a"*(i+1)))
                res.append(modified)
        
        return " ".join(res)