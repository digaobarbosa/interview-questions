# https://leetcode.com/contest/weekly-contest-291/problems/minimum-consecutive-cards-to-pick-up/

from typing import *
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        picked = dict()
        minimum = len(cards)+1
        for i in range(len(cards)):
            c = cards[i]
            if c in picked.keys():
                m = i - picked[c] + 1
                if m < minimum:
                    minimum = m
            picked[c] = i
        return minimum > len(cards) and -1 or minimum

if __name__ == '__main__':
    print(Solution().minimumCardPickup([3,4,2,3,4,7]))
    print(Solution().minimumCardPickup([1,0,5,3]))
    print(Solution().minimumCardPickup([77,10,11,51,69,83,33,94,0,42,86,41,65,40,72,8,53,31,43,22,9,94,45,80,40,0,84,34,76,28,7,79,80,93,20,82,36,74,82,89,74,77,27,54,44,93,98,44,39,74,36,9,22,57,70,98,19,68,33,68,49,86,20,50,43]),3)
