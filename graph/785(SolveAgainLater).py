# 785. Is Graph Bipartite?
# Medium

# hint 
# BFS - use of queue, etc

from type import List
from collections import deque



class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        arr = [-1] * len(graph)

        for i in range(len(graph)):
            if arr[i] != -1:
                continue
            q = deque([(i, 0)])

            while q:
                node, color = q.popleft()
                if arr[node]==-1:
                    arr[node] = color

                    for nei in graph[node]:
                        q.append((nei, color^1))
                if arr[node] != color:
                    return False
        return True





# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false




# class Solution:
#     def isBipartite(self, graph: List[List[int]]) -> bool:
#         odd = [0] * len(graph) # map node i -> odd = 1, even = -1

#         def bfs(i):
#             if odd[i]:
#                 return True
#             q = deque([i])
#             odd[i] = -1
#             while q:
#                 i = q.popleft()
#                 for nei in graph[i]:
#                     if odd[i] == odd[nei]:
#                         return False
#                     elif not odd[nei]:  
#                         q.append(nei)
#                         odd[nei] = -1 * odd[i]
#             return True
        
#         for i in range(len(graph)):
#             if not bfs(i):
#                 return False
#         return True



# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false


