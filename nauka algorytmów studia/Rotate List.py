class Solution(object):
    def rotateRight(self, head:Optional[ListNode], k:int) -> Optional[ListNode]:
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head==None or head.next==None:

            return head

        length: int = 0

        currentNode: Optional[ListNode] = head

        while currentNode!=None:

            length+=1
            currentNode=currentNode.next

        k = k % length
        
        if k == 0:
            return head
        
        currentNode=head
        
        for i in range(length-k-1):

            currentNode=currentNode.next

        newHead=currentNode.next
        
        currentNode.next=None


        tailNode=newHead

        while tailNode.next is not None:
            tailNode=tailNode.next

        
        tailNode.next=head
        head=newHead

        return head