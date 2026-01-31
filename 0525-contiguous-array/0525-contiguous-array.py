class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_index = {}   # stores prefix_sum -> first index
        prefix_sum = 0
        max_length = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                prefix_sum += 1
            else:
                prefix_sum -= 1

            if prefix_sum == 0:
                max_length = i + 1
            elif prefix_sum in prefix_index:
                max_length = max(max_length, i - prefix_index[prefix_sum])
            else:
                prefix_index[prefix_sum] = i

        return max_length
