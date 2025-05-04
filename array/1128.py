class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        c = Counter()
        res = 0
        for d in dominoes:
            key = tuple(sorted(d))
            c[key]+=1
        
        for cnt in c.values():
            res += cnt * (cnt-1)//2

        return res
