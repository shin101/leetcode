class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        total = len(s)
        cnt = 0
        for char in s:
            if char == letter:
                cnt +=1
        
        return math.floor(cnt/total * 100)