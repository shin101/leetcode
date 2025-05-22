class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_order = { char:idx for idx, char in enumerate(order)}

        for idx,w in enumerate(words):
            temp = []
            for i in w:
                temp.append(alien_order[i])
            words[idx] = (temp)

        for i in range(1, len(words)):
            if words[i-1] > words[i]:
                return False
        
        return True
