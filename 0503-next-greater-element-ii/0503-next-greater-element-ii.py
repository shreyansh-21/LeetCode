class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []  # will store indices

        for i in range(2 * n):
            curr = nums[i % n]

            # Pop from stack while current element is greater
            while stack and nums[stack[-1]] < curr:
                res[stack.pop()] = curr

            # Only push indices from the first pass
            if i < n:
                stack.append(i)

        return res
    
        