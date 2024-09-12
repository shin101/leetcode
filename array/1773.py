class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0
        for t, c, n in items:
            if ruleKey == "color":
                if c == ruleValue:
                    res += 1
            elif ruleKey == "type":
                if t == ruleValue:
                    res +=1
            elif ruleKey == "name":
                if n == ruleValue:
                    res+=1
        
        return res