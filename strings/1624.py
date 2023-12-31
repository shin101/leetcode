class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hashmap = {} # letter : idx
        cnt = -1

        for idx, char in enumerate(s):
            if char in hashmap:
                cnt = max(cnt, idx-hashmap[char]-1)
            else:
                hashmap[char] = idx
        return cnt