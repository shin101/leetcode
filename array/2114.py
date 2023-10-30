class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        output = 0
        for sentence in sentences:
            x = len(sentence.split())
            output = max(output, x)
        return(output)
