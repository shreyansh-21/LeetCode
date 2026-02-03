class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        length = len(nums)
        if length < 4:
            return False

        index = 0

        # Phase 1: strictly increasing
        while index + 1 < length and nums[index] < nums[index + 1]:
            index += 1

        if index == 0 or index == length - 1:
            return False

        peak_index = index

        # Phase 2: strictly decreasing
        while index + 1 < length and nums[index] > nums[index + 1]:
            index += 1

        if index == peak_index or index == length - 1:
            return False

        # Phase 3: strictly increasing again
        while index + 1 < length and nums[index] < nums[index + 1]:
            index += 1

        return index == length - 1
