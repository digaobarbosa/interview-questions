# https://leetcode.com/problems/maximal-square/description/?envType=study-plan-v2&envId=top-interview-150
from typing import *


"""
Its DP problem, so we can look at it from the recursion perspective to break down the problem.

if size matrix =1 and value =1. maximal_square=1

We can infer the rule that for maximal_square[i][j] 
1 1 1
1 1 1
1 1 1

maximal_square matrix would be
9 4 1
4 4 1
1 1 1

For a 16 area square
16 9 4 1
9  9 4 1
4  4 4 1
1  1 1 1

I understood that is easier to save the square side, as it grow linearly. So the 16 positions square would be:

4 3 2 1
3 3 2 1
2 2 2 1
1 1 1 1



"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maximal_square = [[0 for j in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]
        maximum_size = 0
        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix[0])-1,-1,-1):
                if matrix[i][j]=='0': # 0 matrix, no square
                    maximal_square[i][j] = 0
                elif maximal_square[i+1][j]==0 or maximal_square[i][j+1]==0:
                    # any of neighbors 0, means at most 1
                    maximal_square[i][j] = 1
                else:
                    maximal_square[i][j] = min(maximal_square[i+1][j], maximal_square[i][j+1],maximal_square[i+1][j+1])+1
                if maximum_size < maximal_square[i][j]:
                    maximum_size = maximal_square[i][j]
        return maximum_size*maximum_size

if __name__ == '__main__':
    print(Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    print(Solution().maximalSquare([["0","1"],["1","0"]]))
    print(Solution().maximalSquare([['0']]))
    print(Solution().maximalSquare([['1']]))

