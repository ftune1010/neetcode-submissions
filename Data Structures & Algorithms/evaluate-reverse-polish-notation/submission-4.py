class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "+-*/":
                d2 = stack.pop()
                d1 = stack.pop()
                if t == "+":
                    res = d1 + d2
                if t == "-":
                    res = d1 - d2
                if t == "*":
                    res = d1 * d2
                if t == "/":
                    res = int(d1 / d2)
                stack.append(res)
            else:
                stack.append(int(t))
        return stack[0]
        