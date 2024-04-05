#https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
from typing import *
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count =0
        for i in range(len(nums)-1,-1,-1) :
            if nums[i] == val:
                nums[i] = nums[-1-count]
                count += 1
        return len(nums) - count




if __name__ == '__main__':
    a = [1,2,3,3]
    r = Solution().removeElement(a,2)
    print(a,r)



