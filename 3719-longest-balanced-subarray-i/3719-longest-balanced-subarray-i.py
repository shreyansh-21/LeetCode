class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        max_len = 0

        for i in range(len(nums)):
            even = set()
            odd = set()

            for j in range(i, len(nums)):
                if nums[j] % 2 == 0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])

                if len(even) == len(odd):
                    max_len = max(max_len, j - i + 1)

        return max_len
