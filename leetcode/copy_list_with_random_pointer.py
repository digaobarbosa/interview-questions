# https://leetcode.com/problems/copy-list-with-random-pointer/?envType=study-plan-v2&envId=top-interview-150

from typing import *

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

"""We can understand as a recursive solution with memorization so that we dont end up in a infinite loop."""

class Solution:

    def rec(self, memory:dict, node):
        if id(node) in memory:
            return memory[id(node)]
        if node is None:
            return None
        r = Node(node.val)
        memory[id(node)] = r
        r.next = self.rec(memory,node.next)
        r.random = self.rec(memory, node.random)
        return r
    def copyRandomList(self, head ) :
        cache = dict()
        r = self.rec(cache,head)
        return r

if __name__ == '__main__':
    n3 = Node(3)
    t = Node(1, Node(2, n3),n3)
    s = Solution().copyRandomList(t)
    print(s)

    #[[7,null],[13,0],[11,4],[10,2],[1,0]]
    n0, n1, n2, n3,n4 = Node(7), Node(13), Node(11), Node(10), Node(1)
    n0.next=n1
    n1.next=n2
    n2.next=n3
    n3.next=n4

    n1.random = n0
    n2.random = n4
    n3.random=n2
    n4.random = n0
    ss = Solution().copyRandomList(n0)
    print(ss)