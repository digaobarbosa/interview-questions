# https://leetcode.com/problems/last-stone-weight-ii/description/
from typing import *


class Solution:
    """
    Try a strategy where we get the biggest stone and smash with the "middle" stone
    """
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        # try to split both
        target = total_sum // 2
        cache = {}
        def dfs(i,total):
            if (i,total) in cache:
                return cache[(i,total)]
            if total >= target or i == len(stones):
                return abs((total) - (total_sum - total))
            r = min(
                dfs(i+1,total), dfs(i+1,total+stones[i])
            )
            cache[(i,total)] = r
            return r
        return dfs(0,0)


#[1,1,2, 4,7,  8] -> [1,1,2,4,7,8]

# [8,2,1,1] x [7,4] -> [2,1,1,1] x[4] -> [1,1,1] x [2] -> [1,1] -> [1] -> [1]

# [21,26,31,33,40]
# [7] x [12]



if __name__ == '__main__':
    print(Solution().lastStoneWeightII([2, 7, 4, 1, 8, 1]))
    print(Solution().lastStoneWeightII([1]))
    print(Solution().lastStoneWeightII([1, 1]))
    print(Solution().lastStoneWeightII([21,26,31,33,40]))
