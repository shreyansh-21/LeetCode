class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = []
        m = {}
        
        for currele in range(len(nums2)-1, -1, -1):
            if stack and nums2[currele] < stack[-1]:
                m[nums2[currele]] = stack[-1]
            else:
                while stack and nums2[currele] > stack[-1]:
                    stack.pop()
                if stack:
                    m[nums2[currele]] = stack[-1]
                else:
                    m[nums2[currele]] = -1
            
            stack.append(nums2[currele])  #  always push value
        
        for i in nums1:
            ans.append(m[i])
        return ans
