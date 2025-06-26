from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy_head: ListNode = ListNode(0)
        dummy_head.next = head
        lead_pointer: ListNode = dummy_head
        follow_pointer: ListNode = dummy_head

        for _ in range(n + 1):
            lead_pointer = lead_pointer.next

        while lead_pointer is not None:
            lead_pointer = lead_pointer.next
            follow_pointer = follow_pointer.next

        follow_pointer.next = follow_pointer.next.next

        return dummy_head.next