class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        # Total binary codes possible of size k
        need = 2 ** k  
        seen = set()
        
        # Slide window of length k
        for i in range(n - k + 1):
            substring = s[i:i+k]
            seen.add(substring)
            
            # Early exit if all found
            if len(seen) == need:
                return True
        
        return len(seen) == need
        