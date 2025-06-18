class Solution(object):
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        nodeHead: ListNode = ListNode(0, head)
        nodePrevious: ListNode = nodeHead
        nodeCurrent: Optional[ListNode] = head

        while nodeCurrent:
            is_duplicate = False

            while nodeCurrent.next and nodeCurrent.val == nodeCurrent.next.val:
                is_duplicate = True
                nodeCurrent = nodeCurrent.next

            if is_duplicate:
                nodePrevious.next = nodeCurrent.next
            else:
                nodePrevious = nodePrevious.next

            nodeCurrent = nodeCurrent.next

        return nodeHead.next