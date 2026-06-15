class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        function = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
        }
        stack = []
        for t in tokens:
            if t in function:
                d2 = stack.pop()
                d1 = stack.pop()
                stack.append(function[t](d1, d2))
            else:
                stack.append(int(t))
        return stack[0]
        