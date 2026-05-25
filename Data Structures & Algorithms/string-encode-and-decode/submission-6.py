class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for i in strs:
            res.append(str(len(i)))
            res.append('#')
            res.append(i)
            
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            rng = int(s[i:j])
            res.append(s[j+1:j+1+rng])
            i = j+1+rng
        return res