# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150
from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = 100000
        for p in prices:
            if p < buy_price:
                buy_price = p
            if p - buy_price > max_profit:
                max_profit = p - buy_price
        return max_profit


if __name__ == '__main__':
    print(Solution().maxProfit([7,1,5,3,6,4]),5)
    print(Solution().maxProfit([7,6,4,3,1]),0)
