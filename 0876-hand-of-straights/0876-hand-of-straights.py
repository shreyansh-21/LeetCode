import heapq
from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq = Counter(hand)  # har card ki frequency
        minHeap = list(freq.keys())  # sab unique cards
        heapq.heapify(minHeap)  # min heap bana lo

        while minHeap:
            first = minHeap[0]  # sabse chhota card uthao
            count = freq[first]  # uski frequency dekho

            for i in range(first, first + groupSize):
                if freq[i] < count:
                    return False  # agar kisi card ki zaroorat se kam frequency milti hai
                freq[i] -= count  # required count hata do

                if freq[i] == 0:
                    # agar frequency 0 ho gayi aur wo heap ke top pe hai toh heap se hatao
                    if i != minHeap[0]:
                        return False  # agar out-of-order zero aaya toh galat
                    heapq.heappop(minHeap)

        return True

        