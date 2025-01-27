
from typing import *

class Solution:
    def range_str(self,first,last):
        if first == last:
            return str(first)
        return str(first)+"->"+str(last)

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return []
        if len(nums)==1:
            return [str(nums[0])]
        ranges = []
        first = nums[0]
        last = nums[0]
        for n in nums[1:]:
            if n-last>1:
                ranges.append(self.range_str(first,last))
                first = n
            last = n
        ranges.append(self.range_str(first,last))
        return ranges


if __name__ == '__main__':
    print(Solution().summaryRanges([0,1,2,4,5,7]))
    print(Solution().summaryRanges([0,2,3,4,6,8,9]))
    print(Solution().summaryRanges([0,2,3,4,6,8,9,11]))