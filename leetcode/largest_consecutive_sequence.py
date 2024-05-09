# https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150
from typing import *


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nn = sorted(nums)
        maxcount = count = 1
        last = nums[0]
        print(nn)
        for n in nn:
            if n - last == 0:
                pass
            elif n - last == 1:
                count += 1
            else:
                if maxcount < count:
                    maxcount = count
                count = 1

            last = n
        if count > maxcount:
            maxcount = count
        return maxcount


if __name__ == '__main__':
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]), 4)
    print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)
