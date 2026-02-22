class Solution:
    def binaryGap(self, n: int) -> int:
        binary_str = bin(n)[2:]
        if binary_str.count('1') <= 1:
            return 0
        
        current_zero_count = 0
        max_gap = 0
        
        for bit in binary_str:
            if bit == '0':
                current_zero_count += 1
            elif bit == '1':
                max_gap = max(max_gap, current_zero_count + 1)
                current_zero_count = 0
        return max_gap