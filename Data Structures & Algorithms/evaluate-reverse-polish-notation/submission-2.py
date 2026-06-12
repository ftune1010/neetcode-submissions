class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        expressions = {
            "+": lambda x, y : x + y,
            "-": lambda x, y : x - y,
            "*": lambda x, y : x * y,
            "/": lambda x, y : int(x / y)
        }
        stack = []
        for s in tokens:
            if s in expressions:
                d2 = stack.pop()
                d1 = stack.pop()
                stack.append(expressions[s](d1, d2))
            else:
                stack.append(int(s))
        return stack[-1]