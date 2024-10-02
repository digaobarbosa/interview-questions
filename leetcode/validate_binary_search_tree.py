# https://leetcode.com/problems/validate-binary-search-tree/description/
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def is_valid(root:Optional[TreeNode], min_value:int, max_value:int) -> bool:
            if root is None:
                return True
            if min_value is not None and root.val <= min_value:
                return False
            if max_value is not None and root.val >= max_value:
                return False            
            return is_valid(root.left, min_value, root.val) and is_valid(root.right, root.val,max_value)
        
        
        if root is None:
            return True
        return is_valid(root.left,None,root.val) and is_valid(root.right, root.val,None)
        

if __name__ ==  '__main__':
    s = Solution()
    print(s.isValidBST(TreeNode(5,TreeNode(4),TreeNode(6,TreeNode(3),TreeNode(7)))))