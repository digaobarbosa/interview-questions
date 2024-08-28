# https://leetcode.com/problems/k-closest-points-to-origin/

from typing import *
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for (x,y) in points:
            heapq.heappush(heap,(x**2 + y**2,[x,y]))
        result = [point for d,point in heapq.nsmallest(k,heap)]
        return result

if __name__ == '__main__':
    print(Solution().kClosest([[1,3],[-2,2]],1))
    print(Solution().kClosest([[-5,4],[-6,-5],[4,6]],2))


