class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        max_heap = [-c for c in c.values()]
        heapq.heapify(max_heap)

        q = deque()
        time = 0 

        while max_heap or q:
            time += 1

            if max_heap:
                popped = heapq.heappop(max_heap)+1
                if popped:
                    q.append([popped, n+time])
            
            if q and time == q[0][1]:
                heapq.heappush(max_heap,q.popleft()[0])

        
        return time 
