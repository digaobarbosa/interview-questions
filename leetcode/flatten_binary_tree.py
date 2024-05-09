# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/?envType=study-plan-v2&envId=top-interview-150
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, node: TreeNode, result: List[TreeNode]):
        if node is None:
            return
        result.append(node)
        self.dfs(node.left, result)
        self.dfs(node.right, result)

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        result: List[TreeNode] = []
        self.dfs(root, result)
        for i in range(1, len(result)):
            parent = result[i - 1]
            node = result[i]
            parent.left = None
            parent.right = node


def print_list(node: TreeNode) -> List[int]:
    res = []
    while node is not None:
        res.append(node.val)
        node = node.right
    return res


if __name__ == '__main__':
    node = TreeNode(1, TreeNode(2), TreeNode(3))
    Solution().flatten(node)
    print(print_list(node))
