# https://leetcode.com/problems/reverse-nodes-in-k-group/?envType=study-plan-v2&envId=top-interview-150

from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    """
    We should reverse k at a time. Initially it seems that we can go iterating on the list with a counter and when it reaches k
    it swaps the current item with the start of this rotation.

    When thinking about how to write this, and the operations that need to be done, it can be better to iterate using the previous
    node as pointer. This way, we can change where it points to.

    Another thing that can help is to create a fake head node, to facilitate the algorithm to be more homogeneous.

    Reverse time!
    it's the more complicated part, we can iterate from start to end keeping pointers to previous node, current node, after node.
    Each iteration we make current.next = prev
    And the last iteration when current=end, we need fix the first and last pointers and make start,end work for the next group.
    start and end can start the next walking iteration with the first value of this one (start.next)

    """

    def reverse_list(self, head:Optional[ListNode], end:Optional[ListNode]):
        prev = head
        ptr = head.next
        while ptr != end:
            after = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = after
        end.next = prev
        head.next = None
        return (end,head)



    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        if k == 1:
            return head
        fake_head = ListNode(0, head)
        start = fake_head
        end = fake_head
        count = 0
        while end is not None:
            if count % k == 0 and count > 0:
                after = end.next
                s,e = self.reverse_list(start.next,end)
                start.next = s
                e.next = after
                start = end = e
                count = 0
            else:
                count += 1
                end = end.next
        return fake_head.next


if __name__ == '__main__':
    # last = ListNode(6)
    # nlist = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, last)))))
    # res,_ = Solution().reverse_list(nlist,last)
    # while res is not None:
    #     print(res)
    #     res = res.next



    nlist = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = Solution().reverseKGroup(nlist,5)
    while res is not None:
        print(res)
        res = res.next
