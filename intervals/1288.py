class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i:(i[0],-i[1]))
        prev = [intervals[0]]

        print(intervals)

        for i in range(1, len(intervals)):
            if intervals[i][0]>=prev[-1][0] and intervals[i][1] <=prev[-1][1]:
                continue
            else:
                prev.append(intervals[i])
        
        return len(prev)


