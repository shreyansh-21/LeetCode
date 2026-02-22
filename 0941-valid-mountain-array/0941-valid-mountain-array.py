class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        i = 0

        # climb up
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == n - 1:
            return False

        # climb down
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        return i == n - 1