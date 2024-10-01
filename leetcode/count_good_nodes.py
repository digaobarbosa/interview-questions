# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self) -> str:
        return str(self.val)

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root:TreeNode, maxpath:int) -> int:
            if root is None:
                return 0
            left = dfs(root.left,max(maxpath,root.val))
            right = dfs(root.right,max(maxpath,root.val))
            if maxpath <= root.val:
                return left + right + 1
            else:
                return left + right
        return dfs(root,-20000)

from collections import deque
def build_tree(arr: List[int]) -> TreeNode:
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        current = queue.popleft()

        if i < len(arr) and arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i += 1

    return root
        



def print_tree_by_levels(root: TreeNode):
    if not root:
        print("[]")
        return

    queue = deque([root])
    all_levels = []

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            if node:
                level.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                level.append("null")

        # Remove trailing "null" values
        while level and level[-1] == "null":
            level.pop()

        if level:  # Only add non-empty levels
            all_levels.append(level)

    # Print each level on a separate line
    print("Tree printed by levels:")
    for i, level in enumerate(all_levels):
        print(f"Level {i}: [{', '.join(level)}]")
    


if __name__=='__main__':
    s = Solution()
    
    # print(s.goodNodes(build_tree([3,1,4,3,None,1,5])),4)
    # print(s.goodNodes(TreeNode(3,TreeNode(1,TreeNode(3)),TreeNode(4,TreeNode(1),TreeNode(5)))),4)
    # print(s.goodNodes(TreeNode(3,TreeNode(3,TreeNode(4),TreeNode(2)))),3)
    # print(s.goodNodes(TreeNode(1)),1)
    # print(s.goodNodes(TreeNode(5,TreeNode(4,TreeNode(3)))),1)
    # print(s.goodNodes(TreeNode(5,TreeNode(4,TreeNode(3)))),1)
    p = build_tree([-1,5,-2,4,4,2,-2,None,None,-4,None,-2,3,None,-2,0,None,-1,None,-3,None,-4,-3,3,None,None,None,None,None,None,None,3,-3])
    # print_tree_by_levels(p)
    print(s.goodNodes(p),5)
