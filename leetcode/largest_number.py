# https://leetcode.com/problems/largest-number/description/
import functools
from typing import *

def order_s(a:str,b:str) -> int:
    if int(a +b) > int(b + a):
        return -1
    if int(a + b) < int(b + a):
        return 1
    return 0

class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        snums = map(str,nums)
        snums = sorted(snums,key=functools.cmp_to_key(order_s))
        res = ''.join(snums)
        if res and res[0] =='0':
            for i in range(len(res)):
                if res[i] != '0':
                    return res[i:]
            return '0'
        return res



if __name__ == '__main__':
    print(Solution().largestNumber([10,2]),"210")
    print(Solution().largestNumber([3,30,34,5,9]),"9534330")