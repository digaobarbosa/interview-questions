# https://leetcode.com/problems/non-overlapping-intervals/description/

from typing import *


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        count = 0
        overlap = intervals[0]
        for i in range(1,len(intervals)):
            it = intervals[i]
            if overlap[1] <= it[0]:
                overlap = it
            elif overlap[1] < it[1]:
                # erasing it interval
                count += 1
            elif overlap[1] >= it[1]:
                # erasing overlap interval
                overlap = it
                count+=1
        return count

s = Solution()
print(s.eraseOverlapIntervals([[1,2],[2,4],[4,5]]),0)
print(s.eraseOverlapIntervals([[1,2],[2,4],[4,5],[1,3]]),1)
print(s.eraseOverlapIntervals([[1,4],[2,4],[4,5],[1,3]]),2)