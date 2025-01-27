import collections
from typing import *

#Brute force with hash map
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        for k,v in counter.items():
            if v == 1:
                return k
        return -1





if __name__ == '__main__':
    print(Solution().singleNumber([2,2,3,2]),3)
    print(1&1)
    print(1&1&1)
    print(2&2&2)
    print(2^2)
    print(0^5)