class Solution:

    def encode(self, strs: List[str]) -> str:

        final = "["
        for i in range(len(strs)):
            if i == len(strs) -1:
                final += f"\"{strs[i]}\""
            else:
                final+= f"\"{strs[i]}\","
        final += "]"

        return final


    def decode(self, strs: str) -> List[str]:

        final = []
        flag = False
        temp = ""
        for i in range(len(strs)):
            if strs[i] == "\"" and flag == False:
                flag = True
                continue
            if strs[i] == "\"" and flag == True:
                flag = False
                final.append(temp)
                temp = ""
                continue
            if flag:
                temp += strs[i]
                
        return final


        
