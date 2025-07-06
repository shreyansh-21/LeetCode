import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasklist = Counter(tasks)
        heap = []
        
        # Use max heap: push negative frequencies
        for freq in tasklist.values():
            heapq.heappush(heap, -freq)
        
        
        time = 0
        queue = deque()  # cooldown queue: (ready_time, freq)
        
        while heap or queue:
            time += 1
            
            if heap:
                freq = heapq.heappop(heap)
                freq += 1  # we add because freq is negative
                if freq != 0:
                    queue.append((time + n, freq))
            
            # If any task is ready to come back from cooldown
            if queue and queue[0][0] == time:
                ready_time, freq = queue.popleft()
                heapq.heappush(heap, freq)
        
        return time
