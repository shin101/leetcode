class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for letter in s:
            if letter != "*":
                stack.append(letter)
            else:
                if stack:
                    stack.pop()
                else:
                    continue
        return "".join(stack)
                    
