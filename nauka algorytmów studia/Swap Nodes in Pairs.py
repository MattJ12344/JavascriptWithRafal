class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cos = ListNode(0, head)
        prev, ktos = cos, head

        while ktos and ktos.next:
            lol = ktos.next.next
            second = ktos.next

            second.next = ktos
            ktos.next = lol
            prev.next = second

            prev = ktos
            ktos = lol
        
        return cos.next