class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) < 3:
            return max(nums)
        heap = []
        s = set()
        for num in nums:
            if num not in s:
                heapq.heappush(heap, num)
                s.add(num)

                if len(heap) > 3:
                    heapq.heappop(heap)
        return heap[0]
