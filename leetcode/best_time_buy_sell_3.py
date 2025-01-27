# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/?envType=study-plan-v2&envId=top-interview-150

from typing import *

class SolutionDFS:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dfs(i:int,price:Optional[int],count:int):
            key = (i,price,count)
            if key in cache:
                return cache[key]
            if i==len(prices) or count>1:
                return 0
            res = None
            if price is not None:
                if prices[i] > price:
                    res = max(prices[i]-price + dfs(i+1,None,count+1),dfs(i+1,price,count))
                else:
                    res = dfs(i+1,price,count)
            else:
                res = max(dfs(i+1,prices[i],count),dfs(i+1,None,count))
            cache[key] = res
            return res
        r = dfs(0,None,0)
        print(cache)
        return r

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy1_price = 100_000
        max_profit1_price = 0
        min_buy2_price = 100_000
        max_profit2_price = 0
        for p in prices:
            min_buy1_price = min(min_buy1_price,p)
            max_profit1_price = max(max_profit1_price,p-min_buy1_price)
            min_buy2_price = min(min_buy2_price,p - max_profit1_price)
            max_profit2_price = max(max_profit2_price,p - min_buy2_price)
        return max_profit2_price



if __name__ == '__main__':
    print(Solution().maxProfit([1,2,3,4,5]),4)
    print(Solution().maxProfit([1,2,3,4,5,1,3]),6)
    print(Solution().maxProfit([3,3,5,0,0,3,1,4]),6)
