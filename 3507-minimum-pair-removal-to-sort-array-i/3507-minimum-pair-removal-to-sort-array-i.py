class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        answer = 0

        while any(nums[i] > nums[i + 1] for i in range(len(nums) - 1)):
            min_sum = float("inf")
            index = 0

            for i in range(len(nums)-1):
                s = nums[i]+nums[i+1]
                if s <min_sum:
                    min_sum = s
                    index = i
            #merge and shift
            nums[index] = min_sum
            nums.pop(index+1)#pop the previous one
            answer +=1
        return answer

