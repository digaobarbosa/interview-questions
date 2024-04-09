# https://leetcode.com/problems/search-insert-position/?envType=study-plan-v2&envId=top-interview-150

from typing import *


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        p = (end)//2
        while start < p < end:
            if target < nums[p]: # right position is to the left of p
                end = p
                p = start + (end-start)//2
            elif target > nums[p]: # right position is to the right of p
                start = p
                p = start + (end-start)//2
            else:
                break
        return p if target <= nums[p] else p+1
