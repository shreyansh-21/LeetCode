class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        
        def check(mid_y: float, total: float) -> bool:
            bot_area = 0.0
            
            for x, y, l in squares:
                boty = y
                topy = y + l
                
                if mid_y >= topy:
                    # Full square below
                    bot_area += l * l
                elif mid_y > boty:
                    # Partial square below
                    bot_area += (mid_y - boty) * l
            
            return bot_area >= total / 2.0
        
        # Compute total area and search bounds
        low = float('inf')
        high = float('-inf')
        total = 0.0
        
        for x, y, l in squares:
            total += l * l
            low = min(low, y)
            high = max(high, y + l)
        
        # Binary search for answer
        result_y = 0.0
        
        while high - low > 1e-5:
            mid = (low + high) / 2.0
            result_y = mid
            
            if check(mid, total):
                high = mid
            else:
                low = mid
        
        return result_y
