# https://leetcode.com/problems/min-cost-to-connect-all-points/description/
import collections
from typing import *

import heapq
class Solution:


    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(i,j):
            return abs(points[i][0]- points[j][0]) + abs(points[j][1]-points[i][1])

        q = points.copy()
        visited = {0}
        min_cost = 0
        hq = [(dist(0,i),i) for i in range(1,len(points))]
        heapq.heapify(hq)
        while len(visited) < len(points) and hq:
            d,index = heapq.heappop(hq)
            if index not in visited:
                visited.add(index)
                min_cost += d
                for i in range(1,len(points)):
                    if i not in visited:
                        heapq.heappush(hq,(dist(index,i),i))
        return min_cost



if __name__ == '__main__':
    print(Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))