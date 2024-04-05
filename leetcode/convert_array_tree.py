# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/?envType=study-plan-v2&envId=top-interview-150
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val) + " " + str(self.left) + " " + str(self.right)


class Solution:
    def rec(self, nums, start, end) -> Optional[TreeNode]:
        if start > end - 1:
            return None
        if start == end - 1:
            return TreeNode(nums[start])
        N = end - start
        middle = N // 2
        root = TreeNode(nums[start+middle-1])
        root.left = self.rec(nums, start, start+middle-1)
        root.right = self.rec(nums, start+middle , end)
        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        N = len(nums)
        middle = N // 2 if N % 2 == 0 else (N + 1) // 2
        root = TreeNode(nums[middle-1])
        root.left = self.rec(nums, 0, middle-1)
        root.right = self.rec(nums, middle , N)
        return root


if __name__ == '__main__':
    print(Solution().sortedArrayToBST([-10,-3,0,5,9]))
