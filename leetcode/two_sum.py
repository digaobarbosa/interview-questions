#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150
from typing import *
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pLeft = 0
        pRight = len(numbers)-1
        while pLeft < pRight:
            s = numbers[pLeft]+numbers[pRight]
            if s == target:
                return [pLeft+1,pRight+1]
            elif s < target:
                pLeft += 1
            elif s > target:
                pRight -=1
        return []


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15],9),[1,2])
    print(s.twoSum([2,3,4],6),[1,3])