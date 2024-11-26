import collections
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

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = collections.defaultdict(lambda : [])
        def dfs(i,current:List):
            if i == len(nums):
                li = result[len(current)]
                if len(li) == 0 or li[-1] != current:
                    li.append(current.copy())
                result[len(current)] = li
                return
            current.append(nums[i])
            dfs(i+1,current)
            current.pop()
            dfs(i+1,current)
        dfs(0,[])
        return [it for li in result.values() for it in li]

if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([4,4,4,1,4]))
    print(Solution2().subsetsWithDup([4,4,4,1,4]))
