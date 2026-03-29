class Solution:

    def encode(self, strs: list[str]) -> str:
        return "".join([str(len(s))+"#"+s for s in strs])

    def decode(self, s: str) -> list[str]:
        if s == "null":
            return []
        index = 0
        result = []
        while index<len(s):
            val = 0
            while s[index]!="#":
                val *= 10
                val += int(s[index])
                index += 1
            result.append(s[index+1: index+val+1])
            index += (val+1)
        return result
            
