#https://leetcode.com/problems/surrounded-regions/

from typing import *
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        q = deque()
        savers = set(([(0,j) for j in range(len(board[0])) if board[0][j]=='O']
         + [(len(board)-1,j) for j in range(len(board[0])) if board[len(board)-1][j]=='O']
         + [(i,0) for i in range(len(board)) if board[i][0]=='O']
         + [(i,len(board[0])-1) for i in range(len(board)) if board[i][len(board[0])-1]=='O']))
        q.extend(savers)
        while q:
            (i,j) = q.pop()
            if i > 0 and board[i-1][j]=='O' and (i-1,j) not in savers:
                savers.add((i-1,j))
                q.append((i-1,j))
            if i < len(board)-1 and board[i+1][j] == 'O' and (i+1,j) not in savers:
                savers.add((i+1,j))
                q.append((i+1,j))
            if j > 0 and board[i][j-1]=='O' and (i,j-1) not in savers:
                savers.add((i,j-1))
                q.append((i,j-1))
            if j < len(board[0])-1 and board[i][j+1]=='O' and (i,j+1) not in savers:
                savers.add((i,j+1))
                q.append((i,j+1))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i,j) not in savers:
                    board[i][j] = 'X'





if __name__ == '__main__':
    # b = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    # Solution().solve(b)
    # print(b)

    b = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
    Solution().solve(b)
    print(b)