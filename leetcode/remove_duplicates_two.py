#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import *

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 1
        v = nums[0]
        i = 1
        final_s = 1
        while i < len(nums):
            if nums[i] != v:
                nums[final_s] = nums[i]
                final_s += 1
                c = 1
                v = nums[i]
            else:
                if c < 2:
                    nums[final_s] = v
                    final_s +=1
                c += 1
            i += 1
        return final_s


if __name__ == '__main__':
    a = [1,1,1,1,2,2,2,3]
    r = Solution().removeDuplicates(a)
    print(a,r)