class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed = {"}":"{",")":"(","]":"["}
        for p in s:
            if p in closed:
                if stack and stack[-1] == closed[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return not stack