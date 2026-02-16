class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for _ in range(32):
            result <<= 1          # Shift result left
            result |= (n & 1)    # Add last bit of n
            n >>= 1              # Shift n right
        
        return result
        