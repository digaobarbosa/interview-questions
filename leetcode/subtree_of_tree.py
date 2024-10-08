# https://leetcode.com/problems/subtree-of-another-tree/
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSame(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (root is None and subRoot is not None) or (subRoot is None and root is not None):
            return False
        if root is None and subRoot is None:
            return True
        if root.val == subRoot.val:
            return self.isSame(root.left,subRoot.left) and self.isSame(root.right,subRoot.right)
        return False
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (root is None and subRoot is not None) or (subRoot is None and root is not None):
            return False
        if root is None and subRoot is None:
            return True
        if root.val == subRoot.val:
            res = self.isSame(root.left,subRoot.left) and self.isSame(root.right,subRoot.right)
            if res: return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)
        


if __name__ == '__main__':
    s = Solution()
    print(s.isSubtree(TreeNode(1),TreeNode(1)),True)
    print(s.isSubtree(TreeNode(1),TreeNode(2)),False)
    print(s.isSubtree(TreeNode(1,TreeNode(2)),TreeNode(2)),True)
    print(s.isSubtree(TreeNode(3,TreeNode(4,TreeNode(1)),TreeNode(5,TreeNode(2))),TreeNode(3,TreeNode(1),TreeNode(2))),False)
        