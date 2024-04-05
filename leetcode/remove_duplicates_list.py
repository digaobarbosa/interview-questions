# Definition for singly-linked list.
from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next is None:
            return str(self.val)
        else:
            return str(self.val)+', '+str(self.next)


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        result = None
        prev = head
        ptr = head
        while ptr is not None:
            #print(str(prev) + ' || '+str(ptr)+ ' || '+ str(result))
            if ptr.val == (ptr.next and ptr.next.val):
                remov = ptr.val
                while ptr is not None and ptr.val == remov:
                    ptr = ptr.next
                if result is None:
                    if prev.val == remov:
                        prev = ptr
                    else:
                        result = prev
                        prev.next = ptr
                else:
                    prev.next = ptr
            else:
                if result is None:
                    result = prev
                if prev != ptr:
                    prev = prev.next
                ptr = ptr.next

        return result




if __name__ == '__main__':
    s = Solution()
    print(s.deleteDuplicates(ListNode(1,ListNode(2,ListNode(2,ListNode(3,ListNode(3,None)))))))
    print(s.deleteDuplicates(ListNode(1,ListNode(1,ListNode(2,ListNode(2,ListNode(3,None)))))))
