# https://leetcode.com/problems/valid-sudoku/?envType=study-plan-v2&envId=top-interview-150

from typing import *


def init_set():
    return {'1', '2', '3', '4', '5', '6', '7', '8', '9'}


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # lines
        for i in range(9):
            line = board[i]
            ns = init_set()
            for j in range(9):
                c = line[j]
                if c != '.':
                    if c in ns:
                        ns.remove(c)
                    else:
                        return False

        # columns
        for i in range(9):
            ns = init_set()
            for j in range(9):
                c = board[j][i]
                if c != '.':
                    if c in ns:
                        ns.remove(c)
                    else:
                        return False
        # quarter
        start_list = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
        for start in start_list:
            ns = init_set()
            x, y = start
            for i in range(3):
                line = board[i + x]
                for j in range(3):
                    c = line[j + y]
                    if c != '.':
                        if c in ns:
                            ns.remove(c)
                        else:
                            return False
        return True


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    s = Solution()
    print(s.isValidSudoku(board))

    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(s.isValidSudoku(board))
