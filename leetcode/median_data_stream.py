# https://leetcode.com/problems/find-median-from-data-stream/description/?envType=study-plan-v2&envId=top-interview-150
from typing import *
import heapq


class MedianFinder:
    def __init__(self):
        self.top = []
        self.bottom = []


    def addNum(self, num: int) -> None:
        heapq.heappush(self.bottom, -num)
        heapq.heappush(self.top, -1*heapq.heappop(self.bottom))
        if len(self.top) > len(self.bottom):
            heapq.heappush(self.bottom, -1*heapq.heappop(self.top))

    def findMedian(self) -> float:
        if (len(self.top) + len(self.bottom)) % 2 == 0:
            return (self.bottom[0]*-1 + self.top[0])/2
        else:
            return self.bottom[0] * -1


def test(calls, args):
    o = MedianFinder()
    for i in range(1, len(args)):
        c = calls[i]
        a = args[i]
        r = getattr(o, c)(*a)
        if r:
            print(r)


if __name__ == '__main__':
    args = [[], [1], [2], [], [3], []]
    calls = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
    test(calls, args)

    calls = ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
    args = [[],[-1],[],[-2],[],[-3],[],[-4],[],[-5],[]]
    test(calls, args)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
