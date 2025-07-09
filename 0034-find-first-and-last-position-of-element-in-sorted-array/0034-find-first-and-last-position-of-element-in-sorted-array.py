class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums, target):
            l, r = 0, len(nums) - 1
            left = -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    if nums[m] == target:
                        left = m
                    r = m - 1
            return left

        def findRight(nums, target):
            l, r = 0, len(nums) - 1
            right = -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] > target:
                    r = m - 1
                else:
                    if nums[m] == target:
                        right = m
                    l = m + 1
            return right

        left = findLeft(nums, target)
        right = findRight(nums, target)
        return [left, right]
