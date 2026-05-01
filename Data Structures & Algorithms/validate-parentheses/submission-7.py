class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:

            if c == ')':
                if not bool(stack) == True or stack[-1] != '(':
                    return False
                stack.pop()

            elif c == ']':
                if not bool(stack) == True or stack[-1] != '[':
                    return False
                stack.pop()

            elif c == '}':
                if not bool(stack) == True or stack[-1] != '{':
                    return False
                stack.pop()

            if c == '(' or c =='{' or c == '[':
                stack.append(c)

        return not bool(stack)