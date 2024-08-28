# https://leetcode.com/problems/reverse-linked-list/
from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next:
            return str(self.val) + " - " + str(self.next)
        else:
            return str(self.val)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        node = head
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        return prev


if __name__ == '__main__':
    print(Solution().reverseList(ListNode(1, ListNode(2, ListNode(3)))))
