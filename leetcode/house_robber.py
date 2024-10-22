# https://leetcode.com/problems/house-robber/description/?envType=study-plan-v2&envId=top-interview-150
from typing import *


class Solution:
    def rob(self, nums: List[int]) -> int:
        caching = dict()
        def rec(start, end) -> int:
            if start >= len(nums):
                return 0
            if (start,end) in caching:
                return caching[(start,end)]
            res = max(nums[start] + rec(start + 2, end), rec(start + 1, end))
            caching[(start,end)] = res
            return res

        return rec(0, len(nums))

if __name__ == '__main__':
    s = Solution()
    print(s.rob([1,2,3,1]))
    print(s.rob([2,7,9,3,1]))

