from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        
        values: list[int] = []

        while head:
            values.append(head.val)
            head = head.next

        left: int = 0
        right: int = len(values) - 1

        while left < right:
            if values[left] != values[right]:
                return False
            left += 1
            right -= 1

        return True
sol = Solution()

# Test 1
assert sol.isPalindrome(None) == True

# Test 2
node1 = ListNode(1)
assert sol.isPalindrome(node1) == True

# Test 3
a = ListNode(1)
b = ListNode(2)
c = ListNode(2)
d = ListNode(1)
a.next = b
b.next = c
c.next = d
assert sol.isPalindrome(a) == True

# Test 4
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(2)
e = ListNode(1)
a.next = b
b.next = c
c.next = d
d.next = e
assert sol.isPalindrome(a) == True

# Test 5
a = ListNode(1)
b = ListNode(2)
a.next = b
assert sol.isPalindrome(a) == False


print("nuda")