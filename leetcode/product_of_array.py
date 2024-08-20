# https://leetcode.com/problems/product-of-array-except-self/
from typing import *
class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [None for n in nums]
        suffix = [None for n in nums]
        for i in range(1,len(nums)):
            previous = nums[i-1]
            if prefix[i-1] is not None:
                prefix[i] = prefix[i-1]*previous
            else:
                prefix[i] = previous

        prefix[0]=1
        for i in range(len(nums)-2,-1,-1):
            previous = nums[i+1]
            if suffix[i+1] is not None:
                suffix[i] = suffix[i+1] * previous
            else:
                suffix[i] = previous
        suffix[len(nums)-1] = 1
        array = [prefix[i]*suffix[i] for i in range(len(nums))]
        return array

class Solution:
    def productExceptSelf(self,nums:List[int]):
        array = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            array[i] = prefix
            prefix = nums[i]*prefix

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            array[i] *= postfix
            postfix *= nums[i]
        return array


if __name__ == '__main__':
    print(Solution().productExceptSelf([1,2,3,4]))
    print(Solution().productExceptSelf([-1,1,0,-3,3]))





