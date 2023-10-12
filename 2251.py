from typing import List
import heapq, heap

# heaps
# for each person in people
# while flowers beginning is less than or equal to person
# while flowers end is less than person, pop


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        
        people = [(p, i) for i, p in enumerate(people)]
        res = [0] * len(people)

        flowers.sort()
        end = []

        j = 0 # curr flower position
        for p, i in sorted(people):
            while j < len(flowers) and flowers[j][0] <= p:
                heapq.heappush(end, flowers[j][1])
                j += 1
            while end and end[0] < p:
                heapq.heappop(end)

            res[i] = len(end)
        return res

# TEST CASE
# Input: flowers = [[1,6],[3,7],[9,12],[4,13]], poeple = [2,3,7,11]
# Output: [1,2,2,2]
# Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
# For each person, we return the number of flowers in full bloom during their arrival.