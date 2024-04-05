# https://leetcode.com/problems/reverse-bits/?envType=study-plan-v2&envId=top-interview-150
from typing import *

class Solution:
    def reverseBits(self, n: int) -> int:
        b = '{:032b}'.format(n)
        s = ''.join(reversed(b))
        return int(s,2)



if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(4))
    print(s.reverseBits(16))
    print(s.reverseBits(96))