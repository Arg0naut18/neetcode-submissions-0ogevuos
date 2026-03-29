class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_arr = [nums[0]]*n
        right_arr = [nums[-1]]*n

        for i in range(1, n):
            left_arr[i] = left_arr[i-1] * nums[i]
            right_arr[n-i-1] = right_arr[n-i] * nums[n-i-1]

        for i in range(n):
            left_side = left_arr[i-1] if i>0 else 1
            right_side = right_arr[i+1] if i+1<n else 1
            nums[i] = left_side * right_side
        
        return nums