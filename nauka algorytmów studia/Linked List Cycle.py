class Solution(object):
    def hasCycle(self, head:Optional[ListNode]) -> bool:
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head.next

        while slow != fast:
            
            if not fast or not fast.next:
                return False
            
            slow = slow.next
            fast = fast.next.next

        return True