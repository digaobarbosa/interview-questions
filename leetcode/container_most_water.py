# https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150

from typing import *

"""
The strategy will be to find the maximum area, iterating through 0 to n, and looking for the areas 
to both sides, left and right. So we can choose which column to choose.
The area is always calculated with min(height[i],height[j])*(j-i), n > j > i >=0
And we want to find its maximum.
"""


class Solution_BF:
    def maxArea(self, height: List[int]) -> int:
        maxr = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                r = min(height[i], height[j]) * (j - i)
                if r > maxr:
                    maxr = r
        return maxr


""" For this solution we used a two pointer approach, starting at index 0 and the last index also. We only need to iterate on
the side that has the smaller value (because it is the one that limits the area calculated).

So we start pointers left and right. And go walking them to the middle, using the least tall of the two. And only 
replacing the max_result if the area calculation is higher for the new positions.

We can optimize further, avoiding area calculation, if we calculate it only when it has the possibility of winning (new_height > than previous pointer height).
"""
class Solution:
    def area(self, height, i, j):
        return min(height[i], height[j]) * abs(j - i)

    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxr = self.area(height, left, right)
        ok_left, ok_right = height[left], height[right]
        while left < right:
            h_left = height[left]
            h_right = height[right]
            if h_left <= h_right:
                left += 1
                if height[left] < ok_left:
                    continue
                a = self.area(height, left, right)
                if a > maxr:
                    maxr = a
                    ok_left = height[left]
            else:
                right -= 1
                if height[right] < ok_right:
                    continue
                a = self.area(height,left,right)
                if a > maxr:
                    maxr = a
                    ok_right = height[right]
        return maxr


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
    print(Solution().maxArea([1, 1]), 1)
    print(Solution().maxArea([1, 2]), 1)
    print(Solution().maxArea([1, 2, 1000]), 2)
