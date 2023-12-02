class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        mapped = {}
        res = 0 

        for c in chars:
            mapped[c] = mapped.get(c, 0) +1
        print(mapped)
        
        for word in words:
            mapped2 = {}
            good = True
            for letter in word:
                mapped2[letter] = mapped2.get(letter, 0) + 1

                if letter not in mapped or mapped2[letter] > mapped[letter]:
                    good = False
                    break
        
            if good:
                res += len(word)

        return res
            
