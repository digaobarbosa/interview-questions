# https://leetcode.com/problems/gas-station/description/?envType=study-plan-v2&envId=top-interview-150

from typing import *

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr = -1
        i = 0
        s = 0
        while i < len(gas):
            isum = 0
            j = i
            has_break = False
            while j < len(gas):
                g = gas[j] - cost[j]
                isum += g
                if isum < 0:
                    i = j
                    has_break = True
                    break
                j += 1
            s += isum
            if not has_break and j == len(gas):
                return  i if s >= 0 else -1
            i += 1
        return -1

if __name__ == '__main__':
    print(Solution().canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]),3)
    print(Solution().canCompleteCircuit([2,3,4],[3,4,3]),-1)





