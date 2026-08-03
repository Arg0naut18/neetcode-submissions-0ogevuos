class Solution:
    def pick(self, nums: List[int], target: int, low: int):
        result = []
        temp = low
        low = low+1
        high = len(nums)-1
        while low<high:
            curr = nums[low]+nums[high]
            if curr==target:
                result.append([nums[temp], nums[low], nums[high]])
                low+=1
            elif curr<target:
                low += 1
            else:
                high -= 1
        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        for i in range(len(nums)):
            res = self.pick(nums, -1*nums[i], i)
            if len(res)>0:
                for l in res:
                    if l not in results:
                        results.append(l)
        return results