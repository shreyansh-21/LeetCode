class Solution:
    def findMaxLength(self, nums):
        maxLen = 0
        prefixSum = 0
        hashmap = {0 : -1}

        for i in range(len(nums)):
            if nums[i] == 0:
                prefixSum += (-1)
            else:
                prefixSum += nums[i]

            if prefixSum in hashmap:
                maxLen = max(maxLen, (i - hashmap[prefixSum]))
                continue

            hashmap[prefixSum] = i

        return maxLen