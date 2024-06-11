class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        c = Counter(arr1)
        diff = []

        for num in arr1:
            if num not in arr2:
                diff.append(num)

        for num in arr2:
            res.extend([num] * c[num])

        diff.sort()
        
        res.extend(diff)

        return res