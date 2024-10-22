# https://leetcode.com/problems/minimum-absolute-difference-in-bst/?envType=study-plan-v2&envId=top-interview-150

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(t:Optional[TreeNode]):
            diff = 1000000
            MIN = 1000000
            MAX = -1
            if t is None:
                return (diff,MIN,MAX) # difference, min value, max value
            if t.left:
                diff1,MIN,max_val = dfs(t.left)
                diff = min(t.val - max_val,diff,diff1)
            if t.right:
                diff2,min_val,MAX = dfs(t.right)
                diff = min(min_val - t.val,diff,diff2)
            return (diff,min(MIN,t.val),max(MAX,t.val))
        return dfs(root)[0]

if __name__ == '__main__':
    s = Solution()
    print(s.getMinimumDifference(TreeNode(4,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(6))))
    print(s.getMinimumDifference(TreeNode(1,None,TreeNode(3,TreeNode(2)))))