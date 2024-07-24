class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        source = defaultdict(int)
        output = defaultdict(int)

        if n==1:
            return 1

        for src, dst in trust:
            source[src] += 1
            output[dst] += 1
        
        # source = {1: 1, 2: 1}
        # output = {2: 1, 3: 1}
        # [[1,2],[2,3]]

        # judge must be not in source key but in output key

        print(source)
        print(output, 'fff')

        # for judge, output should be zero 


        for person in trust:
            if person[1] not in source.keys() and person[1] in output.keys() and output[person[1]] == n-1:
                return person[1]


        return -1



