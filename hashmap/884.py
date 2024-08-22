class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res = []
        s1 = s1.split()
        s2 = s2.split()
        print(s1)
        print(s2)
        combined = s1+s2
        print(combined)
        c = Counter(combined)
        print(c)
        for item in c:
            if c[item] == 1:
                res.append(item)
        return res