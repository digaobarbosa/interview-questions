from typing import *
# https://leetcode.com/problems/path-sum/description/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return targetSum == root.val
        left = self.hasPathSum(root.left, targetSum - root.val)
        if left:
            return True
        right = self.hasPathSum(root.right, targetSum - root.val)
        if right:
            return True
        return False





