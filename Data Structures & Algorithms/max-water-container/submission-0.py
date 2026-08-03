class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i, j = 0, n - 1
        result = 0
        while i<j:
            result = max(min(heights[i], heights[j])*(j-i), result)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return result
