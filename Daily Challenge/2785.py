class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        output = ""

        ascii_sorted = sorted([char for char in s if char in vowels])
        print(ascii_sorted)
        
        i = 0
        for letter in s:
            if letter not in vowels:
                output+=(letter)
            else:
                output+=(ascii_sorted[i])
                i+=1
        return output