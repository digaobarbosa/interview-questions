# https://leetcode.com/problems/binary-tree-level-order-traversal/description/?envType=study-plan-v2&envId=top-interview-150
import queue
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''As it's always the case with trees, a recursive algorithm can work.
So, the idea here is to have a recursive function that receives the node, its current level, and the result list of lists for it to work with'''

class SolutionRec:
    def rec(self, root: Optional[TreeNode], level:int, result:List[List[int]]):
        if root is None:
            return
        # add value to result at the right level
        if len(result) < level:
            result.append([])
        result[level-1].append(root.val)
        self.rec(root.left,level +1, result)
        self.rec(root.right,level +1, result)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        self.rec(root,1,result)
        return result

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque()
        q.append((root,0))
        result = []
        while q:
            node,level = q.popleft()
            if node is None:
                continue
            if level >= len(result):
                result.append([])
            result[level].append(node.val)
            q.append((node.left, level +1))
            q.append((node.right, level +1))
        return result


if __name__ == '__main__':
    root = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
    result = Solution().levelOrder(root)
    print(result,[[3],[9,20],[15,7]])
    result = Solution().levelOrder(TreeNode(1))
    print(result,[[1]])
    result = Solution().levelOrder(None)
    print(result,[])
