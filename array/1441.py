class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        last_num = target[-1]
        idx = 0

        for num in range(1, last_num+1):
            res.append("Push")
            if num != target[idx]:
                res.append("Pop") 
            else:
                idx+=1

        return res 