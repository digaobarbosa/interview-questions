# https://leetcode.com/contest/weekly-contest-291/problems/k-divisible-elements-subarrays/
"""
# Intuition
First solution I had was more of a brute force, where we iterate through all subarrays, created a string out of it to check if we have seen it before.

Inside this loop, I would iterate through the items in this sublist to count the number of divisible items.

There are other solutions like that on Leetcode

# Approach
Then to improve performance I had to avoid the two inner loops:
1 - iterating through the sublist to make a string key to the done set
2 - avoid the inner loop to count the number of divisible items


## 1. For the string key
This was easier (than item 2), just had to keep the str_key variable and create the key for the set each number at a time. So the key creation at each subarray wen from $$O(n)$$ to $$O(1)$$

## 2. Count of divisible items
The idea is to use a precalculation (DP) right at the start counting the number of divisible items seen on the array until so far.
I opted to make a array of len(nums)+1 so it could work even with start=end of array with the formula below.

count_divisors = div_nums[end+1] - div_nums[start]



# Complexity
- Time complexity:
$$O(n²)$$

- Space complexity:
$$O(n)$$

# Code (final version)
```


class Solution:
    def iterate(self, nums: List[int]):
        done = set()
        for start in range(len(nums)):
            str_key = ''

            for size in range(len(nums) - start):
                str_key += ','+str(nums[start+size])
                if str_key in done:
                    continue
                else:
                    done.add(str_key)
                    yield (start,start+size)
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        div_nums = [0] * (len(nums) + 1)
        div_count = 0
        for i in range(len(nums)):
            if nums[i] % p == 0:
                div_count += 1
            div_nums[i + 1] = div_count

        count = 0
        for it in self.iterate(nums):
            # is divisible by p at most k
            count_div = div_nums[it[1]+1] - div_nums[it[0]]
            if count_div <= k:
                count += 1
        return count

```

# Brute Force Code (1st version)
```

class Solution_Brute_force:
    def iterate(self, nums: List[int]):
        done = set()
        for i in range(1, len(nums) + 1):
            for j in range(len(nums) + 1 - i):
                res = nums[j:j + i]
                str_res = ','.join(map(str, res))
                if str_res in done:
                    continue
                else:
                    done.add(str_res)
                    yield res

    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        count = 0
        for it in self.iterate(nums):
            # is divisible by p at most k
            count_div = 0
            for i in it:
                if i % p == 0:
                    count_div += 1
                if count_div > k:
                    break
            if count_div <= k:
                count += 1
        return count
```

"""
from typing import *
import itertools


class Solution_Brute_force:
    def iterate(self, nums: List[int]):
        done = set()
        for i in range(1, len(nums) + 1):
            for j in range(len(nums) + 1 - i):
                res = nums[j:j + i]
                str_res = ','.join(map(str, res))
                if str_res in done:
                    continue
                else:
                    done.add(str_res)
                    yield res

    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        count = 0
        for it in self.iterate(nums):
            # is divisible by p at most k
            count_div = 0
            for i in it:
                if i % p == 0:
                    count_div += 1
                if count_div > k:
                    break
            if count_div <= k:
                count += 1
        return count


class Solution:
    def iterate(self, nums: List[int]):
        done = set()
        for start in range(len(nums)):
            str_key = ''

            for size in range(len(nums) - start):
                str_key += ','+str(nums[start+size])
                if str_key in done:
                    continue
                else:
                    done.add(str_key)
                    yield (start,start+size)
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        div_nums = [0] * (len(nums) + 1)
        div_count = 0
        for i in range(len(nums)):
            if nums[i] % p == 0:
                div_count += 1
            div_nums[i + 1] = div_count

        count = 0
        for it in self.iterate(nums):
            # is divisible by p at most k
            count_div = div_nums[it[1]+1] - div_nums[it[0]]
            if count_div <= k:
                count += 1
        return count


"""
 nums = [2, 4 , 2]
 div_nums = [1, 2, 3]
 div_nums[2] - div_nums[0] + 1 = 3
 
 nums = [2, 4 , 1]
 div_nums = [1, 2, 2]
 div_nums[2] - div_nums[0] + 1 = 2
 
 nums = [1,1,1]
 div_nums = [0,0,0]
 div_nums[2] - div_nums[0] + 1 = 1 ?
 
 -- using i+1
 nums = [2, 4 , 1]
 div_nums = [0,1,2,2]
 div_nums[3] - div_nums[0] = 2
 
 nums = [1,1,1]
 res = 0
 
 formula
 div_nums[end+1] - div_nums[start] 
 
 Also works for nums = [2, 4 , 2] res = 3
 
 Does it work for one position? i=j=0?
 div_nums[1]-div_nums[0]
 
 
"""





if __name__ == '__main__':
    print(Solution().countDistinct([2,3,3,2,2],2,2),11)
    print(Solution().countDistinct([1,2,3,4],4,1),10)
    print(Solution().countDistinct([1, 9, 8, 7, 19], 1, 6),15)
    print(Solution().countDistinct([10,2,17,7,20], 1, 10),14)
