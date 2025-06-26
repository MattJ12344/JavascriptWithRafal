
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


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
    
node1 = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node2.random = node1
node3.random = node5
node4.random = node3
node5.random = node1

s = Solution()
copied = s.copyRandomList(node1)

assert copied.val == 7
assert copied.next.val == 13
assert copied.next.random.val == 7
assert copied.next.next.val == 11
assert copied.next.next.random.val == 1
assert copied.next.next.next.random.val == 11
assert copied.next.next.next.next.random.val == 7

print("Nuda")