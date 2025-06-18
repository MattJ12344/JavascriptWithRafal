# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        nodeHead: ListNode = ListNode(0, head)
        currentNode: ListNode = nodeHead

        while currentNode:
            while currentNode.next and currentNode.next.val == val:
                currentNode.next = currentNode.next.next
            currentNode = currentNode.next
        
        return nodeHead.next