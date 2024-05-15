# https://leetcode.com/problems/single-number/?envType=study-plan-v2&envId=top-interview-150

from typing import *
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r = 0
        for n in nums:
            r = r ^ n
        return r


if __name__ == '__main__':
    pass