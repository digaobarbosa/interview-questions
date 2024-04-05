# https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150


from typing import *


class Solution1:
    def candy(self, ratings: List[int]) -> int:
        min_rating = min(ratings)
        candies = [0 for i in range(len(ratings))]
        count = 0
        for i in range(len(ratings)):
            rate = ratings[i]
            if rate == min_rating:
                candies[i] = 1
                count += 1

        while count < len(ratings):
            for i in range(len(ratings)):
                if candies[i] != 0:
                    continue
                elif len(ratings) - 1 > i > 0:
                    if candies[i - 1] != 0 and candies[i + 1] != 0:
                        rl = ratings[i] > ratings[i - 1] and candies[i - 1] + 1 or 1
                        rr = ratings[i] > ratings[i + 1] and candies[i + 1] + 1 or 1
                        candies[i] = max(rl, rr)
                        count += 1
                elif i == 0:
                    if ratings[i] <= ratings[i + 1]:
                        candies[0] = 1
                        count += 1
                    elif candies[i + 1] > 0:
                        candies[0] = candies[i + 1] + 1
                        count += 1
                elif i == len(ratings) - 1:
                    if ratings[i] <= ratings[i - 1]:
                        candies[-1] = 1
                        count += 1
                    elif candies[i - 1] > 0:
                        candies[-1] = candies[i - 1] + 1
                        count += 1
        return sum(candies)


class Solution:

    def add_neighbor(self, i, candies, to_visit: set):
        if i > 0 and candies[i-1]==0:
            to_visit.add(i - 1)
        if i < len(candies) - 1 and candies[i+1]==0:
            to_visit.add(i + 1)

    def candy(self, ratings: List[int]) -> int:
        candies = [0 for i in range(len(ratings))]
        count = 0
        to_visit = set()
        # cases
        # not bigger than neighbors = 1. First for loop
        # start visiting the ones that had a neighbor change
        # bigger than both neighbors candies[i] = max(neighbors candies) +1
        # bigger than one neighbor and not the other, should not happen
        if len(ratings)==1:
            return 1
        for i in range(len(ratings)):
            if len(ratings)-1 > i > 0 and ratings[i] <= ratings[i-1] and ratings[i] <= ratings[i+1]:
                candies[i] = 1
                count += 1
                self.add_neighbor(i,candies,to_visit)
            elif i==0 and  ratings[0] <= ratings[1]:
                candies[i] = 1
                count += 1
                self.add_neighbor(i,candies,to_visit)
            elif i == len(ratings)-1 and ratings[i] <= ratings[i-1]:
                candies[i] =1
                count += 1
                self.add_neighbor(i, candies,to_visit)


        while to_visit:
            i = to_visit.pop()
            if candies[i] != 0:
                continue
            if 0 < i < len(ratings)-1:
                if (candies[i-1]==0 and ratings[i] > ratings[i-1]) or (candies[i+1]==0 and ratings[i] > ratings[i+1]):
                    continue
                rl = (ratings[i] > ratings[i - 1]) and candies[i - 1] + 1 or 1
                rr = (ratings[i] > ratings[i + 1]) and candies[i + 1] + 1 or 1
                candies[i] = max(rl, rr)
                count += 1
                self.add_neighbor(i,candies,to_visit)
            if i==0 and candies[1]!=0:
                candies[0] = candies[1]+1
            elif i == len(ratings)-1 and candies[i-1]!=0:
                candies[i] = candies[i-1]+1
        print(candies)
        return sum(candies)


if __name__ == '__main__':
    print(Solution().candy([1, 0, 2]))
    print(Solution().candy([1, 2, 2]))
    print(Solution().candy([1,2,87,87,87,2,1]))
