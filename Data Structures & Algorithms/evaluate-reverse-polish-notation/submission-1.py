class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s in "+-*/":
                d2 = stack.pop()
                d1 = stack.pop()
                if s == "+":
                    stack.append(d1 + d2)
                elif s == "-":
                    stack.append(d1 - d2)
                elif s == "*":
                    stack.append(d1 * d2)
                else:
                    stack.append(int(d1 / d2))
            else:
                stack.append(int(s))
            print(stack)
        return stack[-1]