from typing import Optional
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution(object):
    def reverseList(self, head: Optional['ListNode']) -> Optional['ListNode']:
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node:None = None

        while head:
            temp: Optional['ListNode'] = head.next
            head.next = node
            node = head
            head = temp
         
        return node
    
    
sol = Solution()

# Test 1
node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
result = sol.reverseList(node1)
assert result.val == 3 and result.next.val == 2 and result.next.next.val == 1 and result.next.next.next is None

# Test 2
node = ListNode(1)
result = sol.reverseList(node)
assert result.val == 1 and result.next is None

# Test 3
result = sol.reverseList(None)
assert result is None

# Test 4
node2 = ListNode(2)
node1 = ListNode(1, node2)
result = sol.reverseList(node1)
assert result.val == 2 and result.next.val == 1 and result.next.next is None

print("All")