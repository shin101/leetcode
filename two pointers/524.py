class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key= lambda x:(-len(x), x))
        # ['monkey', 'apple', 'plea', 'ale']
       
        for word in dictionary:
            s_pointer = 0
            w_pointer = 0
            while w_pointer < len(word) and s_pointer < len(s):
                if word[w_pointer] == s[s_pointer]:
                    w_pointer += 1
                s_pointer+=1
                if w_pointer == len(word):
                    return word

        return ""