# https://leetcode.com/problems/find-median-from-data-stream/description/?envType=study-plan-v2&envId=top-interview-150
from typing import *
import heapq


class MedianFinder:
    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)

    def findMedian(self) -> float:
        if len(self.heap) % 2 == 1:
            return heapq.nsmallest(len(self.heap) // 2+1, self.heap)[-1]
        else:
            a = heapq.nsmallest(max(len(self.heap) // 2+1,2), self.heap)
            return (a[-1] + a[-2]) / 2


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
