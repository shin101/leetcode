class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        target = ord(target)
        for l in letters:
            curr = ord(l)
            if curr > target:
                return l
        
        return letters[0]
