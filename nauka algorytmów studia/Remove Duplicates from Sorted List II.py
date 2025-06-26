from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        dummy_head: ListNode = ListNode(0, head)
        previous_node: ListNode = dummy_head
        current_node: Optional[ListNode] = head

        while current_node:
            is_duplicate: bool = False

            while current_node.next and current_node.val == current_node.next.val:
                is_duplicate = True
                current_node = current_node.next

            if is_duplicate:
                previous_node.next = current_node.next
            else:
                previous_node = previous_node.next

            current_node = current_node.next

        return dummy_head.next
