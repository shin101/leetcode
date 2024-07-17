class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        c = Counter(nums)
        expected_sum = 0
        duplicate = 0


        for i in range(1, len(nums)+1):
            expected_sum += i

        print(c)

        for k,v in c.items():
            if v > 1 :
                res.append(k)
                duplicate = k
    
        curr_sum = sum(nums) - duplicate


        # curr - sum(nums)
        # expected - 10

        res.append(expected_sum - curr_sum)

        # [2,5]

        return res