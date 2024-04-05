from typing import *

class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 1
        v = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == v:
                c+=1
            elif c > 1:
                c -= 1
            else:
                c=1
                v = nums[i]
        return v

if __name__ == '__main__':
    print(Solution().majorityElement([2,2,1,1,1,2,2]))
    print(Solution().majorityElement([1,1,1]))
    print(Solution().majorityElement([2,2,1,1,1,3,3,3,3,3,3,3]))

