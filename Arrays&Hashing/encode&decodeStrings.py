class Solution:

    def encode(self, strs):
        output = ""
        for i in strs:
            prefix= str(len(i) + "#")
            output = prefix + strs[i]
        return output
        
    def decode(self, s: str):
        pass


    print(encode("ibrahim mohamed talaat"))