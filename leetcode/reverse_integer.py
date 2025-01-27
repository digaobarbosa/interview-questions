# https://leetcode.com/problems/reverse-integer/description/

from typing import *

class Solution:
    MAX = (1<<31) -1
    MIN = -(1<<31)
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] == '-':
            s = s[1:]
        r = int(s[::-1]) * (x < 0 and -1 or 1)
        # print(r,self.MAX)
        if r <= self.MAX and r >= self.MIN:
            return r
        else:
            return 0


if __name__ == '__main__':
    print(Solution().reverse(123),321)
    print(Solution().reverse(778),877)
    print(Solution().reverse(1563847412),0)