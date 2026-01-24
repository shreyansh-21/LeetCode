from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: shifting non-zero elements to the front
        pos = 0
        for num in nums:
            if num != 0:
                nums[pos] = num
                pos += 1
        
        # Step 2: filling rest postion with 0
        for i in range(pos, len(nums)):
            nums[i] = 0