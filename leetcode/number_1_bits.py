# https://leetcode.com/problems/number-of-1-bits/?envType=study-plan-v2&envId=top-interview-150
from typing import *


class Solution:
    def hammingWeight(self, n: int) -> int:
        return '{0:b}'.format(n).count('1')