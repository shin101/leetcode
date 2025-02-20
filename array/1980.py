class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = ""

        for i in range(len(nums)):
            curr = nums[i][i]
            if curr=="0":
                res+="1"
            else:
                res+="0"

        return res 