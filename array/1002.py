class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        first_word = Counter(words[0])
        for w in words:
            temp = Counter(w)
            for letter in first_word:
                first_word[letter] = min(first_word[letter], temp[letter])

        print(first_word)

        for letter in first_word:
            for i in range(first_word[letter]):
                res.append(letter)



# Counter({'l': 2, 'b': 1, 'e': 1, 'a': 1})
        
        return res