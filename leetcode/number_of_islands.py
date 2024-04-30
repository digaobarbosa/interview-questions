# https://leetcode.com/problems/number-of-islands/description/?envType=study-plan-v2&envId=top-interview-150

from typing import *
from collections import deque
class Solution:

    def next_indexes(self,ngrid, visited,ii,jj):
        for i in range(ii,len(ngrid)):
            start_j = i == ii and jj or 1
            for j in range(start_j,len(ngrid[0])):
                if ngrid[i][j]==1 and visited[i][j]== False:
                    return (i,j)
        return (-1,-1)

    def numIslands(self, grid: List[List[str]]) :
        ngrid = [[0]*(len(grid[0])+2) for i in range(len(grid)+2)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ngrid[i+1][j+1] = int(grid[i][j])
        visited = [[False]*(len(grid[0])+2) for i in range(len(grid)+2)]
        q = deque()
        i = 1
        j = 1
        pi,pj = i,j = self.next_indexes(ngrid,visited,i,j)
        count_islands = 0
        if pi >=0:
            q.append((pi,pj))
            count_islands +=1
        while q:
            pi,pj = q.pop()
            visited[pi][pj] = True
            for ni,nj in [(-1,0),(0,-1),(1,0),(0,1)]:
                if ngrid[pi+ni][pj+nj]==1 and visited[pi+ni][pj+nj]==False:
                    q.append((pi+ni,pj+nj))
            if not q:
                i,j = self.next_indexes(ngrid,visited,i,j)
                if i >=0:
                    q.append((i,j))
                    count_islands+=1
        return count_islands




if __name__ == '__main__':
    # islands = Solution().numIslands(
    #     [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]])
    # print(islands)
    #
    # islands = Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])
    # print(islands)

    islands = Solution().numIslands([["0","1","0"],["1","0","1"],["0","1","0"]])
    print(islands)
