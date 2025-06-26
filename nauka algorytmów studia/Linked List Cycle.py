from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True

sol = Solution()

n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2
assert sol.hasCycle(n1) == False

n3 = ListNode(3)
n4 = ListNode(4)
n3.next = n4
n4.next = n3  # cykl
assert sol.hasCycle(n3) == True

n5 = ListNode(5)
assert sol.hasCycle(n5) == False

n6 = ListNode(6)
n6.next = n6
assert sol.hasCycle(n6) == True

print("Meduza")