# Medium
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# DFS - recursion, need base case
# use hashmap to map course to prereq list


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashMap = {i:[] for i in range(numCourses)}
        visited = set()

        for course, pre in prerequisites:
            hashMap[course].append(pre) # {0:[], 1:[0]}

        def dfs(course):
            if course in visited:
                return False
            if hashMap[course] == []:
                return True

            visited.add(course)

            for pre in hashMap[course]:
                if not dfs(pre): return False
            visited.remove(course)
            hashMap[course] = []
            return True
            
        for course in range(numCourses):
            if not dfs(course): return False

        return True


# {0: [], 1: [0]}
# {0: [1], 1: [0]}

# Test Case
print(canFinish(2, [[1,0]])) # true
print(canFinish(2, [[1,0],[0,1]])) # false
print(canFinish(5, [[0,1],[0,2],[1,3],[1,4],[3,4]])) # true
# Run on Leetcode













# # Solution
# def canFinish(numCourses, prerequisites):
#     # map each course to prereq list
#     preMap = { i:[] for i in range(numCourses) }
#     for course, prereq in prerequisites:
#         preMap[course].append(prereq)

#         # visitSet = all courses along the curr DFS path
#     visitSet = set()
#     def dfs(course):
#         # we detected a loop
#         if course in visitSet:
#             return False
#         if preMap[course] == []:
            # return true
      
#         visitSet.add(course)
#         for prereq in preMap[course]:
#             if not dfs(prereq): return False
#         visitSet.remove(course)
#         preMap[course] = []
#         return True
#     for course in range(numCourses):
#         if not dfs(course): return False
#     return True

# print(canFinish(2, [[1,0]])) # true
# print(canFinish(2, [[1,0],[0,1]])) # false
