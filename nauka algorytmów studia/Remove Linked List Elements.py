# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        cos = ListNode(0, head)
        lista = cos

        while lista:
            while lista.next and lista.next.val == val:
                lista.next = lista.next.next
            lista = lista.next
        
        return cos.next