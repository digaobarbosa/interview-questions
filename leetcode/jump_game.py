# https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150
from typing import *

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        to_visit = {0}
        visited = set()
        while to_visit:
            visit = to_visit.pop()
            if visit in visited:
                continue
            if nums[visit]+ visit >= len(nums)-1:
                return True
            elif nums[visit]>0:
                for el in range(visit+1,visit+nums[visit]+1):
                    to_visit.add(el)
                visited.add(visit)
        return False



if __name__ == '__main__':
    print(Solution().canJump([2,3,1,1,4]))
    print(Solution().canJump([3,2,1,0,4]))