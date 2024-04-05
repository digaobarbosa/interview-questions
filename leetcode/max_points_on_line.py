# https://leetcode.com/problems/max-points-on-a-line/?envType=study-plan-v2&envId=top-interview-150
from typing import *


class Solution:
    '''
    the idea is to get two points, calculate the tangent (a) between them.
    After that, following the formula y = x.a+b we can calculate b getting one of the two points
    b = y - a.x
    we save that on a map, because it's the line the two points are in, and there could be more.
    '''

    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        lines_map = dict()

        for i in range(len(points)):
            ix,iy = points[i]
            for j in range(i+1,len(points)):
                jx,jy = points[j]
                line = (None,jx)
                if jx != ix:
                    t = (jy-iy) / (jx - ix)
                    b = jy - t*jx
                    line = (t,b)
                point_set = lines_map.get(line, set())
                point_set.add(tuple(points[i]))
                point_set.add(tuple(points[j]))
                lines_map[line] = point_set


        return max([len(v) for v in lines_map.values()])

if __name__ == '__main__':
    s = Solution()
    print(s.maxPoints([[1, 1], [2, 2], [3, 3]]), 3)
    print(s.maxPoints([[0, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]), 4)
    print(s.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]), 4)
    print(s.maxPoints([[3,3],[1,4],[1,1],[2,1],[2,2]]), 3)
