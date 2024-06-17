# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/?envType=study-plan-v2&envId=top-interview-150
import heapq
from typing import *

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for e1 in nums1:
            for e2 in nums2:
                e = (-e1-e2,e1,e2)
                r = None
                if len(heap) < k:
                    heapq.heappush(heap,e)
                else:
                    r = heapq.heappushpop(heap,e)
                if r and r[0] == e[0]:
                    break

        return [[e[1],e[2]] for e in heapq.nlargest(k,heap)]

class Solution1:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        i1 = 0
        i2 = 0
        heap = []
        for e1 in nums1:
            for e2 in nums2:
                e = (e1+e2,e1,e2)
                heap.append(e)
        heap.sort()
        return [[e[1],e[2]] for e in heap[:k]]


if __name__ == '__main__':
    print(Solution().kSmallestPairs([1,7,11],[2,4,6],3))
    print(Solution().kSmallestPairs([1,1,2],[1,2,3],2))
    print(Solution().kSmallestPairs([1],[1,2,3],2))
    print(Solution().kSmallestPairs([1,2,4,5,6],[3,5,7,9],3))

