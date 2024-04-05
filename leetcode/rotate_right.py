# Definition for singly-linked list.
from __future__ import annotations
from typing import Optional



class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

   def __str__(self):
       return str(self.val) +", "+ str(self.next)


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        iter = head
        count = 1
        while iter.next is not None:
            iter = iter.next
            count += 1

        for i in range( k % count ):
            last = head
            pre_last = head
            while last.next is not None:
                pre_last = last
                last = last.next
            last.next = head
            pre_last.next = None
            head = last
        return head



if __name__ == '__main__':
    s = Solution().rotateRight(ListNode(1,ListNode(2, ListNode(3, ListNode(4)))),2)
    print(s)
