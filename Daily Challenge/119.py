class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # create temp variables to represent triangle structure
        # do the calculation
        res = [[1]]
        for i in range(1, rowIndex+1):
            temp = [1]*(i+1)

            for j in range(1,len(temp)-1):
                temp[j] = res[-1][j] + res[-1][j-1]
            res.append(temp)

        return res[-1]