class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        soutput, toutput = [], []
        for letter in s:
            if letter == "#":
                if soutput:
                    soutput.pop()
                continue
            else:
                soutput.append(letter)

        for letter in t:
            if letter == "#": 
                if toutput:
                    toutput.pop()
                continue
            else:
                toutput.append(letter)

        print(soutput)
        print(toutput)
        return soutput == toutput

        

