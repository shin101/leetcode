class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        store = {} 
        res = 0

        for r in range(rows):
            key = tuple(grid[r])
            store[key] = store.get(key, 0) + 1

        print(store)

        for c in range(cols):
            col_val = [grid[r][c] for r in range(rows)]
            key = tuple(col_val)
            # print(key)
            if key in store:
                res += store[key]
        return res
