# https://leetcode.com/problems/combination-sum/description/?envType=study-plan-v2&envId=top-interview-150
import itertools
from typing import *


class Solution:
    def rec(self, candidates: List[int], target: int) -> List[List[int]]:
        res: List[List[int]] = []
        for i in range(len(candidates)):
            n = candidates[i]
            if n == target:
                res.append([n])
            if n < target:
                rlists = self.rec(candidates[i:], target - n)
                res.extend([[n]+r for r in rlists])
            if n > target:
                break
        return res


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res: List[List[int]] = []
        candidates.sort()
        return self.rec(candidates, target)


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
    print(s.combinationSum([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]])
    print(s.combinationSum([2], 1), [])
