class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = int("".join([str(d) for d in digits])) + 1
        digits = [int(x) for x in str(digits)]

        return(digits)

