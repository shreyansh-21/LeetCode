class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=r=z=0
        maxlength = 0  
        while r < len(nums):
            if nums[r] == 0:
                z += 1
            # If the number of zeros exceeds k, move the left pointer to shrink the window
            while z > k:
                if nums[l] == 0:
                    z -= 1
                l += 1
            maxlength = max(maxlength, r - l + 1)
            r += 1

        return maxlength
