# https://leetcode.com/problems/snakes-and-ladders/?envType=study-plan-v2&envId=top-interview-150
from typing import *
import heapq


class Solution:
    def to_pair(self, index, board):
        maxi = len(board) * len(board[0])
        if index >= maxi:
            return (None, None)
        i = (len(board) - 1) - index // len(board[0])
        asc_dir = ((len(board) - 1) % 2) == (i % 2) and True or False
        j = index % len(board[0])
        if not asc_dir:
            j = len(board[0]) -1 - j
        return (i, j)

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        heap = []
        heapq.heappush(heap, (0, 0,False,[1]))
        maxi = len(board) * len(board[0])
        visited = [(1000,1000)] * maxi
        final_path = None
        while heap:
            count, ii, jump, path = heapq.heappop(heap)
            visited_jump_index = jump and 1 or 0
            i,j = self.to_pair(ii,board)
            if i is None or (visited[ii][visited_jump_index] <= count):
                continue
            if ii == maxi -1:
                final_path = path
            if jump:
                visited[ii] = (visited[ii][0],count)
            else:
                visited[ii] = (count,visited[ii][1])
            place = board[i][j]
            if place == -1 or jump == True:
                for pi in range(1, 7):
                    if ii+pi < maxi and visited[ii+pi][0] > count + 1:
                        heapq.heappush(heap,(count+1,ii+pi,False, path + [ii+pi+1]))
            else:
                placei = place - 1
                heapq.heappush(heap,(count,placei,True, path + [placei+1]))

        return min(visited[-1]) == 1000 and -1 or min(visited[-1])



if __name__ == '__main__':
    print(Solution().snakesAndLadders( # 1 - 2 j 36 - 41 j 29 - 35 j 49 [1,2,36,41,29,35,49]
        [[-1,-1,-1,-1,48,5,-1], #+49
         [12,29,13,9,-1,2,32], # -42
         [-1,-1,21,7,-1,12,49], # +35
         [42,37,21,40,-1,22,12], # -28
         [42,-1,2,-1,-1,-1,6], # +21
         [39,-1,35,-1,-1,39,-1], # -14
         [-1,36,-1,-1,-1,-1,5]]), 3) # +7
    print(Solution().snakesAndLadders([[-1, -1], [-1, 3]]), 1)
    print(Solution().snakesAndLadders([[-1,-1,-1,-1,-1,-1],
                                       [-1,-1,-1,-1,-1,-1],
                                       [-1,-1,-1,-1,-1,-1],
                                       [-1,35,-1,-1,13,-1],
                                       [-1,-1,-1,-1,-1,-1],
                                       [-1,15,-1,-1,-1,-1]]
                                      ), 4)
