class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        res = 0
        temp = []
        c = Counter(arr)
        c = sorted(c.items(), key=lambda item:item[1], reverse=True)

        while len(temp) < ((len(arr))//2):
            for num,cnt in c:
                temp.extend([num]*cnt)
                if len(temp) >= ((len(arr))//2):
                    break

        return len(set(temp))
        

