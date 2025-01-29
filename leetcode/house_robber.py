# https://leetcode.com/problems/house-robber/description/?envType=study-plan-v2&envId=top-interview-150
from typing import *


class Solution:
    def rob(self, nums: List[int]) -> int:
        robbed = [False]*(len(nums))
        SIZE = len(nums)

        def rec(i):
            if i == len(nums):
                return 0
            irobbed = robbed[i-1]
            if i == len(nums) -1:
                irobbed = irobbed or robbed[0]
            if irobbed:
                return rec(i+1)
            else:
                robbed[i % SIZE] = True
                m1 = nums[i % SIZE] + rec(i+1)
                robbed[i % SIZE] = False
                m2 = rec(i+1)
                return max(m1,m2)
        return rec(0)


class Solution:

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums)<3:
            return max(nums)
        return max(self.rob2(nums[0:-1]),self.rob2(nums[1:]))

    def rob2(self, nums: List[int]) -> int:
        SIZE = len(nums)
        dp1 = [0] *SIZE # in case robbed
        dp0 = [0] * SIZE # in case not robbed
        for i in range(SIZE):
            # calc dp1
            dp0[i] = max(dp0[(i-1)],dp1[(i-1)])
            dp1[i] = nums[i] + dp0[(i-1)]
        return max(dp0+dp1)









if __name__ == '__main__':
    s = Solution()
    print(s.rob([1,2,3,1]),4)
    # print(s.rob([2,7,9,3,1]))
    print(s.rob([2,3,2]),3)

