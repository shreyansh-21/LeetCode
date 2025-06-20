import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)  # Har number ka count nikaal liya
        heap = []

        for num, freq in c.items():
            heapq.heappush(heap, (freq, num))  # Heap me (count, number) daala
            if len(heap) > k:
                heapq.heappop(heap)  # Agar heap ka size zyada ho gaya to sabse chhoti frequency hata di

        # Ab heap me top k frequent elements bache hain
        return [num for freq, num in heap]
