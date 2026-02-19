class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        seen = set(nums1)     # store nums1 in a set for O(1) lookup
        result = set()        # store unique intersection elements
        for num in nums2:
            if num in seen:
                result.add(num)
        return list(result)