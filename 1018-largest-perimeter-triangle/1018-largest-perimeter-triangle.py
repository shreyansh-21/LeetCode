class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)

        i = 0

        while i < len(nums) - 2:
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
            i += 1
        return 0