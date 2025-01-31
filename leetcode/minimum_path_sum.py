# https://leetcode.com/problems/minimum-path-sum/
from functools import lru_cache
from typing import *
import heapq

class Solution:
    """
    Solution using a heap to choose the best path now.
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        q = [] # (sum,i,j)
        heapq.heappush(q,(grid[0][0],0,0))
        visited_grid = set()
        while q:
            isum,i,j = heapq.heappop(q)
            visited_grid.add((i,j))
            if i == M-1 and j == N-1:
                return isum
            if i < M-1 and (i+1,j) not in visited_grid:
                heapq.heappush(q,(isum+grid[i+1][j],i+1,j))
            if j < N-1 and (i,j+1) not in visited_grid:
                heapq.heappush(q,(isum+grid[i][j+1],i,j+1))
        return -1 # should not be possible




class SolutionDFS:
    """DFS solution"""
    def minPathSum(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        @lru_cache(maxsize=4000)
        def dfs(i,j):
            if i==M-1 and j == N-1:
                return grid[i][j]
            if i >= M or j >= N:
                return -1
            right_val = dfs(i,j+1)
            down_val = dfs(i+1,j)
            if right_val >=0 and down_val>=0:
                return grid[i][j] + min(right_val,down_val)
            if right_val>=0:
                return grid[i][j] + right_val
            if down_val>=0:
                return grid[i][j] + down_val

        return dfs(0,0)


class SolutionDP:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        sum_grid = [[-1]*N for _ in range(M)]
        for i in range(M-1,-1,-1):
            for j in range(N-1,-1,-1):
                down_val = (i == M-1) and -1 or sum_grid[i+1][j]
                right_val = (j == N-1) and -1 or sum_grid[i][j+1]
                if down_val>=0 and right_val>=0:
                    sum_grid[i][j] = min(down_val+grid[i][j], right_val+grid[i][j])
                elif right_val==-1 and down_val==-1:
                    sum_grid[i][j] = grid[i][j]
                elif down_val == -1:
                    sum_grid[i][j] = right_val+grid[i][j]
                elif right_val == -1:
                    sum_grid[i][j] = down_val+grid[i][j]

        return sum_grid[0][0]


if __name__ == '__main__':
    print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]),7)
    print(Solution().minPathSum([[1,2,3],[4,5,6]]),12)