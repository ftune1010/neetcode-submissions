class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start = ans = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[start])
                start += 1
            seen.add(s[i])
            ans = max(ans, len(seen))
        return ans