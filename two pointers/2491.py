class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total = sum(skill)
        skill.sort()
        target = total // (len(skill)//2)
        res = 0

        l = 0
        r = len(skill)-1

        while l<=r:
            if skill[l] + skill[r] == target:
                res += skill[l] * skill[r]
                l+=1
                r-=1
            else:
                return -1
        
        return res