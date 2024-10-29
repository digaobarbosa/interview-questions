# https://leetcode.com/problems/happy-number/

from typing import *

class Solution:
    def isHappy(self, n: int) -> bool:
        found = {-1}
        while n !=1 and n not in found:
            digits = map(int,str(n))
            found.add(n)
            n = sum([d*d for d in digits])

        return n==1

if __name__ == '__main__':
    print(Solution().isHappy(19))
    print(Solution().isHappy(2))
