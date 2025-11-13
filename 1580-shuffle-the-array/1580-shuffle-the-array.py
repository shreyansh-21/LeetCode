class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        i, j = 0, n
        while i < n:
            arr.append(nums[i])
            arr.append(nums[j])
            i += 1
            j += 1
        return arr
