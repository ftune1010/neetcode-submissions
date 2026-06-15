class Solution:
    def isValid(self, s: str) -> bool:
        closed = {"}":"{",")":"(","]":"["}
        stack = []
        for p in s:
            if p in closed:
                if not stack or stack[-1] != closed[p]:
                    return False
                stack.pop()
            else:
                stack.append(p)
        return not stack