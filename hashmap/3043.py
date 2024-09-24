class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        hashset = set()

        for num in arr1:
            while num and num not in hashset:
                hashset.add(num)
                num = num //10
        

        res = 0
        for num in arr2:
            while num and num not in hashset:
                num = num//10
            
            if num:
                res = max(res, len(str(num)))

        return res
