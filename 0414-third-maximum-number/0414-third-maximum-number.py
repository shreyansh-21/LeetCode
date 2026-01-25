class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ans = list(set(nums))
        if len(ans) >= 3:
            ans.remove(max(ans))
            ans.remove(max(ans))
        return max(ans)