class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Step 1: Calculate trailing zeros for each row
        trailing = []
        for row in grid:
            count = 0
            for j in range(n - 1, -1, -1):
                if row[j] == 0:
                    count += 1
                else:
                    break
            trailing.append(count)

        # Step 2: Process each row
        swaps = 0
        for i in range(n):
            # Required trailing zeros for this row
            required = n - i - 1
            # Find a row j >= i with enough zeros
            j = i
            while j < n and trailing[j] < required:
                j += 1
            # If no such row found
            if j == n:
                return -1

            swaps += j - i

            # Step 3: Bring that row up (simulate sorting / bubbling)
            while j > i:
                trailing[j], trailing[j - 1] = trailing[j - 1], trailing[j]
                j -= 1

        return swaps