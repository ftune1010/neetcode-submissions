class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in "})]":
                if not stack:
                    return False
                if p == "}" and stack[-1] != "{": return False
                if p == ")" and stack[-1] != "(": return False
                if p == "]" and stack[-1] != "[": return False
                stack.pop()
            else:
                stack.append(p)
        return not stack