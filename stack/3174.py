class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for char in s :
            stack.append(char)

            if not stack[-1].isalpha() and stack[-2].isalpha():
                stack.pop()
                stack.pop()

        return "".join(stack)

