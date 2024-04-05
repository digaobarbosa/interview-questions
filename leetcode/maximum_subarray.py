from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum

if __name__ == '__main__':
    s = Solution().maxSubArray([5,4,-1,7,8])
    print(s)

