class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        res = cnt = sum([1 for i in range(k) if s[i] in vowels])

        if res!=k:
            for i in range(k, len(s)):
                cnt = cnt + (s[i] in vowels) - (s[i-k] in vowels)
                res = max(res, cnt)

        return res
