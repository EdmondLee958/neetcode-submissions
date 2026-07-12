class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            if n == '+':
                y = stack.pop()
                x = stack.pop()
                stack.append(x + y)
            elif n == '-':
                y = stack.pop()
                x = stack.pop()
                stack.append(x - y)
            elif n == '*':
                y = stack.pop()
                x = stack.pop()
                stack.append(x * y)
            elif n == '/':
                y = stack.pop()
                x = stack.pop()
                stack.append(int(x / y))
            else:
                stack.append(int(n))

        return stack.pop()