# https://leetcode.com/problems/subsets/description/
from typing import *


class Solution_dfs:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def dfs(i:int):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(1 << n):
            subset = []
            for j in range(n):
                if (1 << j) & i > 0:
                    subset.append(nums[j])
            res.append(subset)
        return res    
            

s = Solution()
print(s.subsets([1,2,3,4,5]))
print(s.subsets([1,2,3,4]))
            





            

