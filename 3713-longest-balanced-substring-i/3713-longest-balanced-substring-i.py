class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            freq = [0] * 26

            for j in range(i, n):
                idx = ord(s[j]) - ord('a')  
                freq[idx] += 1

                # Check balance
                vals = [f for f in freq if f > 0]
                if len(set(vals)) == 1:
                    ans = max(ans, j - i + 1)

        return ans
