# https://leetcode.com/problems/find-peak-element/?envType=study-plan-v2&envId=top-interview-150

from typing import *

class Solution_brute:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = nums[i]
            before = nums[i-1] if i >0 else -2**33
            after =  nums[i+1] if i  < len(nums) -1 else -2**33
            if n > before and n > after:
                return i
        return -1


class Solution:
    """
    Solution using binary search to find the peak in log(n) time
    """
    def findPeakElement(self, nums: List[int]) -> int:
        i = len(nums)//2
        left = 0
        right = len(nums)

        while i >= left and i < right:
            n = nums[i]
            before = nums[i-1] if i >0 else -2**33
            after =  nums[i+1] if i  < len(nums) -1 else -2**33
            if n > before and n > after:
                return i
            elif n < before:
                right = i
            elif n < after:
                left = i
            i = (left + right)//2
        return i







if __name__ == '__main__':
    print(Solution().findPeakElement([1,2,3,1]),2)
    print(Solution().findPeakElement([1,2,1,3,5,6,4]),1)
    print(Solution().findPeakElement([-2147483648,-2147483647]),1)
