from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "😂" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        delimiter = "😂"

        while i < len(s):
            # find delimiter
            j = s.find(delimiter, i)

            # get length
            length = int(s[i:j])

            # get word
            start = j + len(delimiter)
            word = s[start : start + length]
            res.append(word)

            # move index
            i = start + length

        return res
