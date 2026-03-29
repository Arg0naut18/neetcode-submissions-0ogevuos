class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        z = 0
        p = 1

        for i in nums:
            if i==0:
                z+=1
                continue
            p *= i

        if z>1:
            return [0]*n

        if z==1:
            return [0 if i != 0 else p for i in nums]

        return [p//i for i in nums]
