# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
    def __str__(self) -> str:
        return str(self.val)
    
    def __repr__(self) -> str:
        return str(self.val)

class Solution_brute:
    def dfs(self,root:TreeNode,p:TreeNode, path:list[TreeNode]):
        if root is None:
            return None
        if root.val == p.val:
            return path+[root]
        res = self.dfs(root.left,p,path+[root])
        if res: return res
        res = self.dfs(root.right,p,path+[root])
        if res: return res
        return None


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pathp = self.dfs(root,p,[])
        pathq = self.dfs(root,q,[])
        previous = None
        for i in range(min(len(pathp),len(pathq))):
            pp = pathp[i]
            pq = pathq[i]
            if pp == pq:
                previous = pp
            else:
                return previous
        return previous

class Solution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        is_pleft = root.val > p.val
        is_qleft = root.val > q.val
        if is_pleft != is_qleft:
            return root
        if is_pleft:
            return self.lowestCommonAncestor(root.left,p,q)
        return self.lowestCommonAncestor(root.right,p,q)
    
def main():

    root = TreeNode(3,TreeNode(1),TreeNode(5))
    res = Solution().lowestCommonAncestor(root, TreeNode(5), TreeNode(1))
    print(res,3)

    root = TreeNode(3,TreeNode(1),TreeNode(5,TreeNode(4),TreeNode(6)))
    res = Solution().lowestCommonAncestor(root, TreeNode(4), TreeNode(5))
    print(res,5)
   



if __name__ == "__main__":
    main()
        