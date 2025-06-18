class Solution(object):
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        nodeHeed: ListNode = ListNode(0)
        nodeHeed.next = head
        leadPointer: ListNode = nodeHeed
        nextPointer: ListNode = nodeHeed

        for _ in range(n + 1):
            leadPointer = leadPointer.next

        while leadPointer is not None:
            leadPointer = leadPointer.next
            nextPointer = nextPointer.next

        nextPointer.next = nextPointer.next.next

        return nodeHeed.next