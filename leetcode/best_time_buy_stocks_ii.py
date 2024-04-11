# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&envId=top-interview-150


from typing import *

""" The idea here is to walk through the prices, and always when we have a lower value than the previous
one we "sell". Adding the current_profit to the total_profit.

So the trader strategy is, buy at the minimum, and sell at the peak. If there is a value smaller than the peak, it will be 
a new buy_price for a possible sell after.

At the end, we need to sell what we have bought at the last price. If the last price was smaller than the previous, it will already be
the buy_price it adds 0 to total_profit. 
"""
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        current_profit = 0
        buy_price = None
        last_price = None
        total_profit = 0
        for p in prices:
            if buy_price is None:
                buy_price = p
                last_price = p
                current_profit = 0
            elif last_price > p:
                total_profit += current_profit
                current_profit = 0
                last_price = p
                buy_price = p
            elif p - buy_price > current_profit:
                current_profit = (p - buy_price)
                last_price = p
        # alway realize at the end
        total_profit +=  prices[-1] - buy_price
        return total_profit


if __name__ == '__main__':
    print(Solution().maxProfit([7,1,5,3,6,4]))
    print(Solution().maxProfit([1,2,3,4,5]))
    print(Solution().maxProfit([7,6,4,3,1]))