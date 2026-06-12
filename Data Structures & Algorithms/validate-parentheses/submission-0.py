class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in "[({":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if s[i] == "}" and stack[-1] != "{": return False
                if s[i] == ")" and stack[-1] != "(": return False
                if s[i] == "]" and stack[-1] != "[": return False
                stack.pop()
        return not stack