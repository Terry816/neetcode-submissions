class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for word in strs:
            res.append(str(len(word)))
            res.append("#")
            res.append(word)

        return "".join(res)

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):
            temp = ""
            j = i
            while s[j] != "#":
                temp += s[j]
                j+=1
            temp = int(temp)
            j += 1
            res.append(s[j:j+temp])
            i = j+temp
        
        return res
