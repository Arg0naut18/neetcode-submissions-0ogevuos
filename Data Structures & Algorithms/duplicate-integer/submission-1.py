class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        digits_occurring_in_nums = set()
        for this_element in nums:
            if this_element not in digits_occurring_in_nums:
                digits_occurring_in_nums.add(this_element)
            else:
                return True
        return False
