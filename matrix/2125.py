class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev = bank[0].count("1")

        for i in range(1, len(bank)):
            curr = bank[i].count("1")
            if curr:
                res += prev*curr
                prev = curr
        return res