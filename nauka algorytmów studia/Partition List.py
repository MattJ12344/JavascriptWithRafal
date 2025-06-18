class Solution(object):
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        slist: Optional[ListNode] = ListNode()
        blist: Optional[ListNode] = ListNode()
        small: Optional[ListNode]= slist
        big: Optional[ListNode] = blist

        while head:
            
            if head.val < x:
                small.next = head
                small = small.next
                
            else:
                big.next = head
                big = big.next

            head = head.next

        small.next = blist.next
        big.next = None

        return slist.next