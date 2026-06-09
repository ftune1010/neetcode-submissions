class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def counter(s: str) -> dict:
            res = {}
            for char in s:
                res[char] = res.get(char, 0) + 1
            return res
        return counter(s) == counter(t)