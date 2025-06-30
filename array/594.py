class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = 0
        c = Counter(nums)

        for num in c:
            if num+1 in c:
                cnt = max(cnt, c[num]+c[num+1])

        return cnt