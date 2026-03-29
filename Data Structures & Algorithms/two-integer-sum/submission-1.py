class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}
        for i, n in enumerate(nums):
            if target-n in mapper:
                return [mapper[target-n], i]
            mapper[n] = i
        return result
