class Solution:

    def encode(self, strs: list[str]) -> str:
        if len(strs)==0:
            return "null"
        return ":->:".join(strs)

    def decode(self, s: str) -> list[str]:
        if s == "null":
            return []
        return s.split(":->:")