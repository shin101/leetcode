class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        cols = len(matrix[0])
        rows = len(matrix)



        mins = set() # 1, 3, 12 ; value : idx. so should be like
        # {1:0, 3:1, 12:3}
        maxes = set()

        for i in range(rows):
            mins.add(min(matrix[i]))
            
        for c in range(cols):
            curr_max = matrix[0][c] # 1, 10 , 4, 2
            for r in range(rows):
                curr_max = max(curr_max, matrix[r][c])
            maxes.add(curr_max)



        return list(mins.intersection(maxes))

    
