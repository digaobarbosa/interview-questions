# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/?envType=study-plan-v2&envId=top-interview-150
from typing import *
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    def __eq__(self, other):
        return other.val == self.val

class Solution:

    def path(self, root:TreeNode, t:TreeNode,path:List) -> Optional[List[TreeNode]]:
        if root is None:
            return None
        if root == t:
            return path + [root]
        left = self.path(root.left,t,path + [root])
        if left is not None:
            return left
        right = self.path(root.right,t,path + [root])
        if right is not None:
            return right
        return None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = self.path(root,p,[])
        q_path = self.path(root,q,[])

        i=0
        lca = None
        while i < len(p_path) and i < len(q_path):
            if p_path[i]==q_path[i]:
                lca=p_path[i]
            else:
                break
            i += 1
        return lca


if __name__ == '__main__':
    node2 = TreeNode(5)
    node3 = TreeNode(4)
    t1 = TreeNode(3, TreeNode(5,TreeNode(6),TreeNode(2,TreeNode(7),TreeNode(4))), TreeNode(1,TreeNode(0),TreeNode(8)))
    t2 = TreeNode(1,TreeNode(2), TreeNode(3))
    s = Solution()
    print(s.lowestCommonAncestor(t1,node2,node3),1)
