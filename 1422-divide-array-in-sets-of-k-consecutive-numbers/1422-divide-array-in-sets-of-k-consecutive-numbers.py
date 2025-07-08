from collections import Counter
import heapq

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        c = Counter(nums)
        heap = list(c.keys())
        heapq.heapify(heap)

        while heap:
            first = heap[0]
            count = c[first]

            for i in range(first, first + k):
                if c[i] < count:
                    return False
                c[i] -= count
                if c[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)
        return True
