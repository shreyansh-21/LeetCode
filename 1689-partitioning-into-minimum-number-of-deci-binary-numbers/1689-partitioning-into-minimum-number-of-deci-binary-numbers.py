class Solution:
    def minPartitions(self, n: str) -> int:
        maxn = 0
        for i in n:
            maxn = max(maxn, int(i))
        return maxn