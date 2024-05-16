# https://leetcode.com/problems/search-a-2d-matrix/?envType=study-plan-v2&envId=top-interview-150

from typing import *


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        n = len(matrix)
        m = len(matrix[0])
        index:int = int(n*m)//2
        min_index = 0
        max_index = n*m
        while index > min_index and index < max_index:
            value = matrix[index // m][index % m]
            if value == target:
                return True
            elif value > target:
                max_index = index
            else:
                min_index = index
            index = (max_index + min_index)//2
        return matrix[index // m][index % m] == target







if __name__ == '__main__':
    print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3),True)
    print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13),False)
    print(Solution().searchMatrix([],13),False)
    print(Solution().searchMatrix([[1,2]],1),True)