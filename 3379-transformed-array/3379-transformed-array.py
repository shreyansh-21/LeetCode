class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        for i in range(n):
            index = (i + nums[i]) % n
            ans[i] = nums[index]

        return ans
