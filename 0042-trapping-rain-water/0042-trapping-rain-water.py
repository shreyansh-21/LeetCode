class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        leftmax = [0] * n   #Array banao
        rightmax = [0] * n
        
        leftmax[0] = height[0] #initial value to everything 
        rightmax[-1] = height[-1]
        i = 1
        j = n - 2

        while i < n and j >= 0:
            leftmax[i] = max(leftmax[i - 1], height[i])
            rightmax[j] = max(rightmax[j + 1], height[j])
            i += 1
            j -= 1
        
        water = 0 # using the minimum from the array and - height
        for k in range(n):
            water += min(leftmax[k], rightmax[k]) - height[k]
        
        return water
