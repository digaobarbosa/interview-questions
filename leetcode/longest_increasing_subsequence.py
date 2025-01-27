# https://leetcode.com/problems/longest-increasing-subsequence/
from typing import *

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memory = [1]*len(nums)
        total_max = 1
        for i,n in enumerate(nums):
            max_sub = 1
            for j in range(0,i):
                nj = nums[j]
                if nj < n and max_sub < memory[j]+1:
                    max_sub = memory[j]+1
            memory[i] = max_sub
            if total_max < max_sub:
                total_max = max_sub
        return total_max



if __name__ == '__main__':
    print(Solution().lengthOfLIS([0,1,0,3,2,3]),4)
    print(Solution().lengthOfLIS([7,7,7,7,7]),1)
    print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]),4)
    print(Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6]),6)
