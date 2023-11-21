class Solution:
    def maxPower(self, s: str) -> int:
        power = curr = 1

        if len(s) == 0 :
            return 0

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr +=1
                power = max(power, curr)
            else:
                curr = 1
        return power
