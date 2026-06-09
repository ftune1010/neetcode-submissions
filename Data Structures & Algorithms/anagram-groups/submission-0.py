class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            key = str(sorted(word))
            if key in res:
                res[key].append(word)
            else:
                res[key] = [word]
        return list(res.values())
