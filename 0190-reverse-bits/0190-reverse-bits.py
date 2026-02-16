class Solution:
    def reverseBits(self, n: int) -> int:
        # Convert to 32-bit binary, reverse, convert back
        b = format(n, '032b')   # 32-bit binary string
        b_rev = b[::-1]         # reverse string
        return int(b_rev, 2)