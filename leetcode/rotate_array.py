#https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150
from typing import *

class SolutionSlow:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            step = 1
            for i in range(len(nums)-step-1,-1,-1):
                tmp = nums[i]
                nums[i] = nums[i+step]
                nums[i+step] = tmp

class Solution:

    def reverse(self, nums: List[int], begin, end):
        while begin < end:
            tmp = nums[begin]
            nums[begin] = nums[end]
            nums[end] = tmp
            begin += 1
            end -= 1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k ==0:
            return

        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums)-1)


if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9]
    Solution().rotate(a,4)
    print(a)
    a = [1,2,3,4,5,6,7]
    Solution().rotate(a,3)
    print(a)
    a = [-1,-100,3,99]
    Solution().rotate(a,2)
    print(a)

    a = [1,2,3,4,5,6]
    Solution().rotate(a,3)
    print(a)


