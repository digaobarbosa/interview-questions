#https://leetcode.com/problems/the-skyline-problem/

from typing import *
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        buildings.sort(key = lambda x: x[0])
        position = (0,0,0)
        result = []
        for bleft,bright,bheight in buildings:
            build = (bleft,bright,bheight)
            
            if position[1] < bleft:
                result.append((position[1],position[2]))
                position =


            print(bleft,bright,bheight)


if __name__ == '__main__':
    print(Solution().getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
