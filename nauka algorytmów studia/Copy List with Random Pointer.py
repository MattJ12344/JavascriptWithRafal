"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head: Node) -> Node:
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        current: Node = head
        while current:
            new_node = Node(current.val, current.next)
            current.next = new_node
            current = new_node.next
            
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        orginalHead:Node = head
        copiedHead:Node = head.next
        currentOrginal:Node = orginalHead
        currentCopied:Node = copiedHead
        
        while currentOrginal:
            currentOrginal.next = currentOrginal.next.next
            currentCopied.next = currentCopied.next.next if currentCopied.next else None
            currentOrginal = currentOrginal.next
            currentCopied = currentCopied.next
            
        return copiedHead