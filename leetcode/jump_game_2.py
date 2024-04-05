# https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150
from typing import *



class Solution:

    def __init__(self):
        self.memory = dict()
    def jump_rec(self, start, nums):
        result = None
        if self.memory.get(start) is not None:
            return self.memory[start]
        size = nums[start]
        if start == len(nums) - 1:
            result = 0
        elif start + size >= len(nums) - 1:
            result = 1
        elif size > 0:
            results = ([self.jump_rec(i, nums) for i in range(start + 1, start + size + 1)])
            filtered = [x for x in results if x is not None]
            if filtered:
                result = min(filtered)+1
            else:
                result = None
        self.memory[start] = result
        return result

    def jump(self, nums: List[int]) -> int:
        return self.jump_rec(0, nums)


if __name__ == '__main__':
    print(Solution().jump([2, 3, 1, 1, 4]))
    print(Solution().jump([0]))
    print(Solution().jump([2, 3, 0, 1, 4]))
