class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        i = 0

        def lower(char):
            if ord(char) < ord('a'):
                char = chr(ord(char) - ord('A') + ord('a'))
            return (char)


            # A -> 1
            # B -> 2
            # C -> 3
            # a -> 100
            # b -> 101
            # c -> 102

        while i < len(s):
            if stack and lower(stack[-1]) == lower(s[i]) and stack[-1]!=s[i] :
                stack.pop()
            else:
                stack.append(s[i])
            
            i += 1


        return "".join(stack)