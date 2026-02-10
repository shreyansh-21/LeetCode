class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = n
        
        for i in range(n):
            xor ^= i ^ nums[i]
        
        return xor
        # We initialize xor = n because:Our loop only goes from 0 → n-1, so we must include n manually.