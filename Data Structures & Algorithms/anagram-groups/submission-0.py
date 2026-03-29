class Solution:
    def hash(self, word) -> str:
        return hash(str(sorted(word)))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = {}
        for s in strs:
            hash_val = self.hash(s)
            if hash_val in mapper:
                mapper[hash_val].append(s)
            else:
                mapper[hash_val] = [s]
        return list(mapper.values())