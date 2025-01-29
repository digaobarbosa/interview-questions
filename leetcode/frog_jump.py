# https://leetcode.com/problems/frog-jump/description/
import collections
from typing import *

class Solution_Regular:
    def canCross(self, stones: List[int]) -> bool:
        q = collections.deque()
        q.append((0,0))
        stone_set = set(stones)
        objective = stones[-1]
        while q:
            last_i,last_k = q.pop()
            next_ks = [last_k-1,last_k,last_k+1]
            for k in next_ks:
                if k > 0 and (k+last_i) in stone_set:
                    if (k + last_i) == objective:
                        return True
                    elif (k + last_i) < objective:
                        q.append((k+last_i,k))
        return False

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)
        objective = stones[-1]
        cache = {}
        def dfs(i,last_k):
            if (i,last_k) in cache:
                return cache[(i,last_k)]

            next_ks = [last_k-1,last_k,last_k+1]
            res = False
            for k in next_ks:
                if k > 0 and (k+i) in stone_set:
                    if (k + i) == objective:
                        return True
                    elif (k + i) < objective:
                       res = res or dfs(k+i,k)
                       if res:
                           break
            cache[(i,last_k)] = res
            return res
        return dfs(0,0)




if __name__ == '__main__':
    print(Solution().canCross([0,1,3,5,6,8,12,17]),True)
    print(Solution().canCross([0,10]),False)




