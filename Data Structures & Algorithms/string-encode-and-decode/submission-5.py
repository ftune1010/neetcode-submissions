class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) +  "_" + word  
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        n = len(s)
        i = 0
        while i < n:
            j = i
            while s[j] != "_":
                j += 1
            steps = int(s[i:j])
            res.append(s[j+1:j+1+steps])
            i = j + steps + 1   
        return res
