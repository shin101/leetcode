class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        q = deque([arr[0], arr[1]])
        curr_max = max(arr[0], arr[1])
        cnt = 1

        if k >= len(arr):
            return max(arr)

        for i in range(2, len(arr)):
            if cnt == k :
                return curr_max

            if arr[i] > curr_max:
                curr_max = arr[i]
                cnt = 1
            else:
                cnt += 1
        return curr_max
        
