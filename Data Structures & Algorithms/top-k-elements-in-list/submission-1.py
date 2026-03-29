class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapper = {}
        result = []

        for n in nums:
            mapper[n] = 1 if n not in mapper else mapper[n]+1

        for l in list(sorted(mapper.items(), key=lambda m: -m[1]))[:k]:
            result.append(l[0])
        
        return result