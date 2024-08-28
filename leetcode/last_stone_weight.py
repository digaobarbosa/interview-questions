# https://leetcode.com/problems/last-stone-weight/description/
from typing import *

import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while heap:
            y = heapq.heappop(heap)
            if len(heap) == 0:
                return -y
            x = heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, y - x)
        return 0


if __name__ == '__main__':
    print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))
    print(Solution().lastStoneWeight([1]))
    print(Solution().lastStoneWeight([1, 1]))
