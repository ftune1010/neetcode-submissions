class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "":
            return ""
        count_t, window = {}, {}
        for i in range(len(t)):
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        l = 0
        res, res_len = [-1, -1], float("inf")
        have, need = 0, len(count_t)
        for r in range(len(s)):
            ch = s[r]
            window[ch] = 1 + window.get(ch, 0)
            if ch in count_t and count_t[ch] == window[ch]:
                have += 1
            while have == need:
                if r - l + 1 < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""
            