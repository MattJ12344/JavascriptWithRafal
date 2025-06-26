from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head

        length: int = 0
        current_node: Optional[ListNode] = head

        while current_node is not None:
            length += 1
            current_node = current_node.next

        k = k % length
        if k == 0:
            return head

        current_node = head
        for _ in range(length - k - 1):
            current_node = current_node.next

        new_head: Optional[ListNode] = current_node.next
        current_node.next = None

        tail_node = new_head
        while tail_node.next is not None:
            tail_node = tail_node.next

        tail_node.next = head
        head = new_head

        return head