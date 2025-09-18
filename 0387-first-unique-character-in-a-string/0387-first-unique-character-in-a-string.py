from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freqcount = Counter(s)
        for i in range(len(s)):
            if freqcount[s[i]] == 1:
                return i
        return -1
