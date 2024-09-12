class Solution:
    def average(self, salary: List[int]) -> float:
        s = min(salary)
        l = max(salary)
        res = 0
        cnt = 0

        for sal in salary:
            if sal!=s and sal!=l:
                res+=sal
                cnt +=1
        return res/cnt

