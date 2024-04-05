from typing import List
import itertools
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = list(sorted(nums))
        combinations = [itertools.combinations(nums,i) for i in range(len(nums)+1)]
        r = [set([i for i in comb]) for comb in combinations]
        res = []
        for group in r:
            for item in group:
                res.append(list(item))
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([4,4,4,1,4]))
