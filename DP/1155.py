class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        cache = {} # (n, target) -> count

        def count(n, target):
            res = 0
            if n == 0:
                return 1 if target == 0 else 0
            if target < 0 :
                return 0
            if (n, target) in cache:
                return cache[(n, target)]
            
            for val in range(1, k+1):
                res = (res + count(n -1 , target - val)) % mod
            cache[(n, target)] = res
            return res
        return count(n, target)