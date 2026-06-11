class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = collections.Counter(s1)
        seen = {}
        l = 0
        for r in range(len(s2)):
            # if s2[r] not in count:
            #     seen = {}
            #     continue
            seen[s2[r]] = 1 + seen.get(s2[r], 0)
            while seen.get(s2[r], 0) > count.get(s2[r], 0):
                seen[s2[l]] -= 1
                if seen[s2[l]] == 0:
                    seen.pop(s2[l])
                l += 1
            if seen == count:
                return True
        return False
        