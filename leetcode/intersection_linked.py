# https://leetcode.com/problems/intersection-of-two-linked-lists/
from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = {str(headA.val):headA}
        pa = headA
        while pa.next:
            if pa.val:
                a[pa.val] = pa
            pa = pa.next

        b = headB
        while b:
            if b.val in a and a[b.val] is b:
                return b
            b = b.next
        return None


