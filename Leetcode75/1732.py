class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        output = [0]

        for num in gain:
            output.append(output[-1]+num)

        return max(output)