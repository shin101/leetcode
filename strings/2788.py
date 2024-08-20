class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []

        for i in range(len(words)):
            words[i] = words[i].split(separator)
        

        for word in words:
            res.extend(word)

        return([x for x in res if x!=""])