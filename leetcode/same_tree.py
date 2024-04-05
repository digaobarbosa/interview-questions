# https://leetcode.com/problems/same-tree/?envType=study-plan-v2&envId=top-interview-150
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        sp = [p]
        sq = [q]
        while sp or sq:
            if len(sp) != len(sq):
                return False
            pp = sp.pop()
            pq = sq.pop()
            if pp == pq:
                return True
            if (pq is None) or (pp is None) or pp.val != pq.val:
                return False
            if (pp.left is None) ^ (pq.left is None):
                return False
            if (pp.right is None) ^ (pq.right is None):
                return False
            if pp.left:
                sp.append(pp.left)
            if pp.right:
                sp.append(pp.right)
            if pq.left:
                sq.append(pq.left)
            if pq.right:
                sq.append(pq.right)
        return True

if __name__ == '__main__':
    t1 = TreeNode(1,TreeNode(2), TreeNode(3))
    t2 = TreeNode(1,TreeNode(2), TreeNode(3))
    s = Solution()
    print(s.isSameTree(t1,t2))


    t1 = TreeNode(1,TreeNode(2))
    t2 = TreeNode(1,None, TreeNode(2))
    s = Solution()
    print(s.isSameTree(t1,t2))
