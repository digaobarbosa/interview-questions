# https://leetcode.com/problems/daily-temperatures/
from typing import  *
import heapq


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        heap = []
        for i,t in enumerate(temperatures):
            while heap and temperatures[heap[-1]] < t:
                hi = heap.pop()
                answer[hi] = i - hi
            heap.append(i)
        return answer


if __name__ == '__main__':
    print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]),[1,1,4,2,1,1,0,0])