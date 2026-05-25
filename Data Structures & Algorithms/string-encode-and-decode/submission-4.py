class Solution:

    def encode(self, strs: List[str]) -> str:

        res = []

        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)

        return "".join(res)

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):
            temp = ""
            j = i
            while s[j] != "#":
                temp += s[j]
                j+= 1
            num = int(temp)
            res.append(s[j+1:j+num+1])
            i = j + num + 1

        return res
