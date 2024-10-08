# https://leetcode.com/problems/permutations/description/
from typing import *

class Solution():
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        



class Solution_rec:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []
        added = set()
        def dfs(n):
            permutation.append(n)
            added.add(n)
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                permutation.pop()
                added.remove(n)
                return
            for i in nums:
                if i not in added:
                    dfs(i)
            added.remove(n)
            permutation.pop()
        for n in nums:
            dfs(n)
        return res
    
s = Solution()
print(s.permute([1,2,3]))

            