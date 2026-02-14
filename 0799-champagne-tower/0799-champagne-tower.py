class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        # Memo table
        t = [[-1.0 for _ in range(101)] for _ in range(101)]
        
        def solve(i, j):
            # Out of bounds
            if i < 0 or j < 0 or j > i:
                return 0.0
            
            # Top glass
            if i == 0 and j == 0:
                t[i][j] = poured
                return t[i][j]
            
            # Memoized
            if t[i][j] != -1.0:
                return t[i][j]
            
            # Overflow from parents
            up_left = (solve(i - 1, j - 1) - 1) / 2.0
            up_right = (solve(i - 1, j) - 1) / 2.0
            
            # Only positive overflow counts
            up_left = max(0.0, up_left)
            up_right = max(0.0, up_right)
            
            t[i][j] = up_left + up_right
            return t[i][j]
        
        # Glass capacity = 1
        return min(1.0, solve(query_row, query_glass))
        