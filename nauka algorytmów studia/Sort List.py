from typing import Optional

class ListNode(object):
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow, fast = head, head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        prev.next = None

        left = self.sortList(head)
        right = self.sortList(slow)
        return self.merge(left, right)

    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        current = dummyHead
        
        while left and right:
            
            if left.val < right.val:
                current.next = left
                left = left.next
                
            else:
                current.next = right
                right = right.next
                
            current = current.next
            
        if left:
            current.next = left
            
        if right:
            current.next = right
            
        return dummyHead.next
    
# Test 1
a = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
res = Solution().sortList(a)
assert [res.val, res.next.val, res.next.next.val, res.next.next.next.val] == [1, 2, 3, 4]

# Test 2
b = ListNode(5)
res = Solution().sortList(b)
assert [res.val] == [5]

# Test 3
c = None
res = Solution().sortList(c)
assert res == None

# Test 4
d = ListNode(2, ListNode(1))
res = Solution().sortList(d)
assert [res.val, res.next.val] == [1, 2]

# Test 5
e = ListNode(3, ListNode(3, ListNode(3)))
res = Solution().sortList(e)
assert [res.val, res.next.val, res.next.next.val] == [3, 3, 3]

# Test 6
f = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
res = Solution().sortList(f)
assert [res.val, res.next.val, res.next.next.val, res.next.next.next.val, res.next.next.next.next.val] == [-1, 0, 3, 4, 5]

# Test 7
g = ListNode(1, ListNode(1, ListNode(1, ListNode(1))))
res = Solution().sortList(g)
assert [res.val, res.next.val, res.next.next.val, res.next.next.next.val] == [1, 1, 1, 1]

# Test 8
h = ListNode(9, ListNode(7, ListNode(5, ListNode(3, ListNode(1)))))
res = Solution().sortList(h)
assert [res.val, res.next.val, res.next.next.val, res.next.next.next.val, res.next.next.next.next.val] == [1, 3, 5, 7, 9]

print("Nuda")