class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        maze[entrance[0]][entrance[1]] == "+"
        visited = set()
        visited.add((entrance[0],entrance[1]))

        q = deque([(entrance[0], entrance[1], 0)])
        while q:
            x,y,d = q.popleft()

            if(x==0 or y==0 or x==m-1 or y==n-1) and [x, y] != entrance:
                return d
            for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if (0 <= i < m) and (0 <= j < n) and maze[i][j]=="." and (i,j) not in visited:
                    q.append((i, j, d+1))
                    visited.add((i,j))

        return -1
