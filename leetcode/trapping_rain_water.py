# https://leetcode.com/problems/trapping-rain-water/

from typing import *


class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0]*len(height)
        max_right = [0]*len(height)
        mleft = 0
        for i in range(len(height)):
            if height[i]> mleft:
                mleft = height[i]
            max_left[i] = mleft
        mright = 0
        for i in range(len(height)-1,-1,-1):
            if height[i] > mright:
                mright = height[i]
            max_right[i] = mright
        total_water = 0
        for i in range(len(height)):
            iw = max(min(max_right[i],max_left[i]) - height[i],0)
            total_water+= iw
        return total_water




"""
Ex 1
[4,2,0,3,2,5] 
walls = [(0,4),(3,3),(5,5)]


Ex 2
[4,2,0,3,2,1,2]
walls = [(0,4),(3,3),(6,2)]
[4,2,2,2,0,0]
e2
Ex 3:
[0,1,0,2,1,0,1,3,2,1,2,1]
[_,1,_,2,_,_,_,3,_,_,2,_]
"""

if __name__ == '__main__':
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
    print(Solution().trap([4, 2, 0, 3, 2, 5]), 9)
    print(Solution().trap([4, 3, 2, 2, 1]), 0)
    print(Solution().trap([1, 2, 3, 4, 4, 3, 2, 2, 1]), 0)
