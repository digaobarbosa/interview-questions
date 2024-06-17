# https://leetcode.com/problems/kth-smallest-element-in-a-bst/?envType=study-plan-v2&envId=top-interview-150
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self._rec_kthSmallest(root,k)[0]


    def _rec_kthSmallest(self, root: Optional[TreeNode], k: int) -> (int,int):
        if root is None:
            return (-1,k)
        s1,c1 = self._rec_kthSmallest(root.left,k)
        if c1 == 0:
            return (s1,c1)
        # print(root.val,c1,k,c1)
        if c1 == 1:
            return (root.val,0)
        s2,c2 = self._rec_kthSmallest(root.right,c1-1)
        return (s2,c2)

if __name__ == '__main__':
    print(Solution().kthSmallest(TreeNode(3,TreeNode(1,None,TreeNode(2)),TreeNode(4)),2))
    print(Solution().kthSmallest(TreeNode(5,
                                          TreeNode(3,
                                                   TreeNode(2,TreeNode(1)),TreeNode(4))
                                          ,TreeNode(6)),3))



