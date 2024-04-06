class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = set()
        res = ""

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')' and stack:
                stack.pop()
            elif char == ')':
                to_remove.add(i)

        to_remove.update(stack)
        print(to_remove)
    

        for i, char in enumerate(s):
            if i not in to_remove:
                res += char

        return res


