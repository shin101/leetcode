class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zipped = list(zip(names, heights))
        sorted_zipped = sorted(zipped, key = lambda zipped:zipped[1], reverse=True)
        return [k for k,v in sorted_zipped]