# https://leetcode.com/problems/sum-root-to-leaf-numbers/?envType=study-plan-v2&envId=top-interview-150
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def dfs(self, root: TreeNode, path: str):
        path = path + str(root.val)
        if root.left is None and root.right is None:
            return int(path)
        total = 0
        if root.left:
            total += self.dfs(root.left, path)
        if root.right:
            total += self.dfs(root.right, path)
        return total

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.dfs(root, '0')


if __name__ == '__main__':
    r = Solution().sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3)))
    print(r,25)
