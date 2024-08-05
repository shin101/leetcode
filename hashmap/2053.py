class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        unique = []

        counter = 0

        for key,v in c.items():
            if v == 1:
                unique.append(key)
                counter += 1
                if counter == k :
                    return key
        
        return ""
