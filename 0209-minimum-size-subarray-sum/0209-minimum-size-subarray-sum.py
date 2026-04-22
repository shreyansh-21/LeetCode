class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        s = 0
        l = 0

        for r in range(len(nums)):
            s += nums[r]

            while s >= target:
                min_length = min(min_length, r - l + 1)
                s -= nums[l]
                l += 1

        return min_length if min_length < float('inf') else 0