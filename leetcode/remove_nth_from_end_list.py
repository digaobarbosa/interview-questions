# https://leetcode.com/problems/remove-nth-node-from-end-of-list/?envType=study-plan-v2&envId=top-interview-150

from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    We first iterate through the list to find the size of it.
    with this size, we can calculate the index that should be removed, and then
    iterate again on the list until the index and remove it.
    To facilitate the process we keep track of the previous node, so it can point to another place.
    And also to facilitate we create a fake head, that avoids edge cases if n==size.
    O(n) complexity
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        ptr = head
        while ptr is not None:
            ptr = ptr.next
            size += 1
        to_remove = size - n

        cur_index = 0
        fake = ListNode(0,head)
        ptr = head
        previous = fake
        while ptr is not None:
            if cur_index == to_remove:
                previous.next = ptr.next
                return fake.next
            previous = ptr
            ptr = ptr.next
            cur_index += 1
        return fake.next


def list_from_nodes(head: Optional[ListNode]) -> list[int]:
    res = []
    ptr = head
    while ptr is not None:
        res.append(ptr.val)
        ptr = ptr.next
    return res


if __name__ == '__main__':
    a = Solution().removeNthFromEnd(ListNode(1,ListNode(2,ListNode(3,ListNode(4)))),1)
    print(list_from_nodes(a),[1,2,3])
    a = Solution().removeNthFromEnd(ListNode(1,ListNode(2,ListNode(3,ListNode(4)))),2)
    print(list_from_nodes(a),[1,2,4])