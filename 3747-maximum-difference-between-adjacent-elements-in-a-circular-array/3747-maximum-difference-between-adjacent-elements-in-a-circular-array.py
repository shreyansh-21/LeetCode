class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        res = abs(nums[n-1]-nums[0])
        for i in range(0,n-1):
            a = abs(nums[i+1]-nums[i])
            if res < a:
                res = a
        return res
        