# https://leetcode.com/problems/3sum/
from typing import *


class SolutionBF:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        return list([list(t) for t in result])


class Solution:
    def two_sum(self, start: int, nums: List[int], target: int):
        end = len(nums) - 1
        result = []
        prev = None
        while start < end:
            if prev == nums[start]:
                start += 1
                continue
            s = nums[start] + nums[end]
            if s < target:
                start += 1
            elif s > target:
                end -= 1
            elif s == target:
                prev = nums[start]
                result.append((nums[start], nums[end]))
                start += 1
        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        prev = None
        result = []
        for i in range(len(nums) - 2):
            if nums[i] == prev:
                continue
            prev = nums[i]
            ts_res = self.two_sum(i + 1, nums, -nums[i])
            if ts_res:
                result.extend([[prev,t0,t1] for t0,t1 in ts_res])
        return result


# print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
# print(Solution().threeSum([-1, 0, 1]))
# print(Solution().threeSum([1, 0, 1]))
print(Solution().threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]), "##",
      [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]])
