# https://leetcode.com/problems/max-area-of-island/description/
from typing import *

class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def count_1(x,y):
            if x < 0 or x > len(grid)-1 or y < 0 or y > len(grid[0])-1:
                return 0
            if grid[x][y] != 1:
                return 0
            grid[x][y] = -1
            return 1 + count_1(x-1,y) + count_1(x+1,y)+ count_1(x,y-1) + count_1(x,y+1)

        max_value = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count = count_1(i,j)
                    if count > max_value:
                        max_value = count
        return max_value




if __name__ == '__main__':
    r = Solution().maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])
    print(r,6)
    r= Solution().maxAreaOfIsland([[1,1],[1,1]])
    print(r,4)
    r= Solution().maxAreaOfIsland([[0,0],[0,0]])
    print(r,0)