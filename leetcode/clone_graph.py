# https://leetcode.com/problems/clone-graph/?envType=study-plan-v2&envId=top-interview-150
from typing import *


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self):
        return str(self.val)


from typing import Optional


class SolutionRec:

    def rec(self, node: Optional['Node'], previous_map: dict[int, 'Node']):
        if node is None:
            return None
        pnode = previous_map.get(node.val)
        if pnode is not None:
            return pnode
        else:
            pnode = Node(node.val)
            previous_map[node.val] = pnode
            pnode.neighbors = [self.rec(n, previous_map) for n in node.neighbors]
            return pnode

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        res = self.rec(node, dict())
        return res


class Solution:

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return None

        queue = [node]
        created_map = {node: Node(node.val)}
        while queue:
            old_node = queue.pop()
            new_node = Node(old_node.val)
            if old_node in created_map.keys():
                new_node = created_map[old_node]
            else:
                created_map[old_node] = new_node

            for n in old_node.neighbors:
                if n in created_map.keys():
                    new_node.neighbors.append(created_map[n])
                else:
                    queue.append(n)
                    new_n = Node(n.val)
                    created_map[n] = new_n
                    new_node.neighbors.append(new_n)

        return created_map[node]


if __name__ == '__main__':
    print(Solution().cloneGraph(Node(1, [Node(2), Node(3)])))
