class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        for i in range(numRows):
            inner = [1] * (i+1)
            output.append(inner)
        
        for j in range(2, numRows):
            for idx in range(1, len(output[j])-1):
                output[j][idx] =  output[j-1][idx] + output[j-1][idx-1]
                
        return output