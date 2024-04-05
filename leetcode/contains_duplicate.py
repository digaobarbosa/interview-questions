#https://leetcode.com/problems/contains-duplicate-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import *
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        value_map = dict()
        for i in range(len(nums)):
            v = nums[i]
            last_index = value_map.get(v)
            if last_index is not None and abs(i - last_index) <= k:
                return True
            else:
                value_map[v] = i
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyDuplicate([1,2,3,1],3),True)
    print(s.containsNearbyDuplicate([1,0,1,1],1),True)
    print(s.containsNearbyDuplicate([1,2,3,1,2,3],2),False)
    print(s.containsNearbyDuplicate([1,2,3,1,2,3],4),True)
