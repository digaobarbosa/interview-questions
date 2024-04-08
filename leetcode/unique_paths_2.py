# https://leetcode.com/problems/unique-paths-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import *


class SolutionRec:
    """We start with a recusive solution that's easier to reason about."""

    def __init__(self):
        self.memory = dict()

    def rec(self, obstacleGrid: List[List[int]], i: int, j: int) -> int:
        if obstacleGrid[i][j] == 1:
            return 0
        # stopping at the objective, returns 1
        if i == len(obstacleGrid) - 1 and j == len(obstacleGrid[0]) - 1:
            return 1
        saved_r = self.memory.get((i,j))
        if saved_r: return saved_r
        # previous positions we have something like
        # bottom way - i iteration
        ic = 0
        if i < len(obstacleGrid) -1 and obstacleGrid[i+1][j]==0:
            ic = self.rec(obstacleGrid,i+1,j)
        # right way - j iteration
        jc = 0
        if j < len(obstacleGrid[0])-1 and obstacleGrid[i][j+1]==0:
            jc = self.rec(obstacleGrid,i,j+1)
        result = ic + jc
        self.memory[(i,j)] = result
        return result


    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.rec(obstacleGrid, 0, 0)




class Solution:
    """We start with a recusive solution that's easier to reason about. But now we can do a DP one.
    We make a table a little bigger than obstacleGrid initialized with 0s (it should make the iteration easier).

    We build paths_grid from the end to the start, put a 1 if it's the objective, and for other positions it's the
    sum of paths for the possible route cells (i,j+1), (i+1,j).
    The result appears on paths_grid[0][0]"""

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        paths_grid = [ [0 for i in range(len(obstacleGrid[0])+1)] for x in range(len(obstacleGrid)+1) ]
        for i in range(len(obstacleGrid)-1,-1,-1):
            for j in range(len(obstacleGrid[0])-1,-1,-1):
                if obstacleGrid[i][j] == 1:
                    continue
                if i==len(obstacleGrid)-1 and j == len(obstacleGrid[0])-1:
                    paths_grid[i][j] = 1
                else:
                    paths_grid[i][j] = paths_grid[i+1][j] + paths_grid[i][j+1]
        return paths_grid[0][0]


if __name__ == '__main__':
    print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 2)
    print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 6)
    print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 1, 0]]), 1)
    print(Solution().uniquePathsWithObstacles([[0, 1], [0, 0]]), 1)
    print(Solution().uniquePathsWithObstacles([[0, 0], [0, 0]]), 2)
    print(Solution().uniquePathsWithObstacles([[1, 0]]), 0)
