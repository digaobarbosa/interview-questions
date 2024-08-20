#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150
from typing import *
class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j] ==  target:
                    return [i,j]
        return []


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        array = sorted([(numbers[i],i) for i in range(len(numbers))])
        pLeft = 0
        pRight = len(numbers)-1
        while pLeft < pRight:
            s = array[pLeft][0]+array[pRight][0]
            if s == target:
                return sorted([array[pLeft][1],array[pRight][1]])
            elif s < target:
                pLeft += 1
            elif s > target:
                pRight -=1
        return []



if __name__ == '__main__':
    s = Solution()
    # print(s.twoSum([2,7,11,15],9),[1,2])
    # print(s.twoSum([2,3,4],6),[1,3])
    print(s.twoSum([3,2,4],6),[1,2])