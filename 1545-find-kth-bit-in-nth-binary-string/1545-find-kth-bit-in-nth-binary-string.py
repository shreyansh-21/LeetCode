class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        
        # Step 1: Build up to Sn
        for _ in range(2, n + 1):
            
            # Invert the string
            inverted = ""
            for ch in s:
                if ch == "0":
                    inverted += "1"
                else:
                    inverted += "0"
            
            # Reverse the inverted string
            reversed_inverted = inverted[::-1]
            
            # Form next string
            s = s + "1" + reversed_inverted
        
        # Step 3: Return kth bit (convert to 0-based index)
        return s[k - 1]