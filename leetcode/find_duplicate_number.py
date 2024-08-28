# https://leetcode.com/problems/find-the-duplicate-number/

from typing import *

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        # numsum = (n+1)*n//2
        # return numsum - sum(nums)
        found = [False]*100001
        for t in nums:
            if found[t]:
                return t
            found[t] = True
        return 0

if __name__ == '__main__':
    print(Solution().findDuplicate([1,3,4,2,2]))
    print(Solution().findDuplicate([3,1,3,4,2]))
    print(Solution().findDuplicate([3,3,3,3,3]))
