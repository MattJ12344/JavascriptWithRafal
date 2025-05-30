class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head==None or head.next==None:

            return head

        l=0

        curr=head

        while curr!=None:

            l+=1
            curr=curr.next

        k = k % l
        if k == 0:
            return head
        curr=head
        for i in range(l-k-1):

            curr=curr.next

        new_head=curr.next
        curr.next=None


        tail=new_head

        while tail.next!=None:
            tail=tail.next

        
        tail.next=head
        head=new_head

        return head