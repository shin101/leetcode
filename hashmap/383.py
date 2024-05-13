class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = Counter(magazine)
        print(magazine)
        for letter in (ransomNote):
            if letter not in magazine:
                return False
            else:
                magazine[letter] -= 1 
                if magazine[letter] < 0 :
                    return False
        
        return True