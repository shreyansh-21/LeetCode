class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26         
        left, max_freq, max_window = 0, 0, 0

        for right in range(len(s)):
            idx = ord(s[right]) - ord('A')
            freq[idx] += 1
            max_freq = max(max_freq, freq[idx])

            # Current window size
            window_size = right - left + 1
            # If replacements needed > k → shrink window
            if window_size - max_freq > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1
            max_window = max(max_window, right - left + 1)

        return max_window