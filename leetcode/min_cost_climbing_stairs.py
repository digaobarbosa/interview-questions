from typing import *


class Solution:
    def minCostClimbingStairs(self, cost: List[int]):
        if len(cost) == 0: return 0
        if len(cost) == 1: return cost[0]
        total_cost = [0] * len(cost)
        for i in range(len(cost) - 1, -1, -1):
            climb1 = 0
            if i + 1 < len(cost):
                climb1 = total_cost[i + 1]
            climb2 = 0
            if i + 2 < len(cost):
                climb2 = total_cost[i + 2]
            total_cost[i] = cost[i] + min(climb1, climb2)
        return min(total_cost[0],total_cost[1])


if __name__ == '__main__':
    print(Solution().minCostClimbingStairs([10,15,20]))
    print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
