class Solution:
    ELEMS = {}

    def check_consequtive(self, start: int, increasing: bool, streak: int = 0) -> int:
        if start not in self.ELEMS:
            return streak
        next_elem = start + 1 if increasing else start - 1
        # print(start, next_elem)
        return self.check_consequtive(next_elem, increasing, streak+1)

    def get_or_default(self, key: int, default_value=0):
        if key not in self.ELEMS:
            return default_value
        return self.ELEMS[key]

    def longestConsecutive(self, nums: List[int]) -> int:
        self.ELEMS = {}
        # print(nums)
        if len(set(nums))<2:
            return len(set(nums))

        for n in nums:
            self.ELEMS[n] = self.get_or_default(n) + self.get_or_default(n-1)+self.get_or_default(n+1)

        # print("ELEMS", self.ELEMS)

        starters = set()
        for n in self.ELEMS.keys():
            if self.ELEMS[n]==0:
                starters.add(n)

        # print("Starters", starters)
        max_len = 1

        for starter in starters:
            # print("Starting max_len evaluation for", starter)
            max_len = max(max_len, self.check_consequtive(starter, True), self.check_consequtive(starter, False))
        return max_len