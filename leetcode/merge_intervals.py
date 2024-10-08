# https://leetcode.com/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-interview-150

from typing import *
class Solution2:
    """
    The idea here is to sort the list first. Than we can keep track of the current result's interval we are creating.
    We keep cur_start,cur_end as the interval to be added on the result.
    And while we walk through the sorted list, we guarantee that we will only have intersection if the
    start of the item is below or the same the cur_end of the interval. If it's above, it makes us
    start a new interval for the result.
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        index = 1
        cur_start = intervals[0][0]
        cur_end = intervals[0][1]
        result = []
        while index < len(intervals):
            start,end = intervals[index]
            if start <= cur_end:
                if end > cur_end:
                    cur_end = end
            else:
                result.append([cur_start,cur_end])
                cur_start = start
                cur_end = end
            index += 1
        result.append([cur_start,cur_end])
        return result


class Solution:
    """
    The idea here is to sort the list first. Than we can keep track of the current result's interval we are creating.
    We keep cur_start,cur_end as the interval to be added on the result.
    And while we walk through the sorted list, we guarantee that we will only have intersection if the
    start of the item is below or the same the cur_end of the interval. If it's above, it makes us
    start a new interval for the result.
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        last = None
        for i in range(len(intervals)):
            it = intervals[i]
            if last is None:
                res.append(it)
                last = it
            elif last[1] < it[0]:
                res.append(it)
                last = it
            elif last[1] >= it[0]:
                last[0] = min(it[0],last[0])
                last[1] = max(it[1],last[1])
        return res



if __name__ == '__main__':
    print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]),[[1,6],[8,10],[15,18]])
    print(Solution().merge([[1,4],[4,5]]),[[1,5]])