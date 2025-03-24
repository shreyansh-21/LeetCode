class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs =0
        ms = -inf
        for num in nums:
            cs = max(cs+num ,num)
            ms = max(cs,ms)
        return ms
        