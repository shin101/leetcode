class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # create adjacency list (neighbors)
        # create maxtime obj, map course:time
        # for each neighbor per course, take max of curr or curr+nei
        # return maxtime[course]
        max_time = {}
        adj = defaultdict(list)

        for crs,dst in relations:
            adj[crs].append(dst)

        def dfs(crs):
            if crs in max_time:
                return max_time[crs]
            res = time[crs-1]
            for nei in adj[crs]:
                res = max(res, time[crs-1] + dfs(nei))
            max_time[crs] = res
            return res

        for i in range(1, n+1):
            dfs(i)
        return max(max_time.values())

