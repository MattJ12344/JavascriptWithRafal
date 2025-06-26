from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        slist = ListNode(0)
        blist = ListNode(0)
        small = slist
        big = blist

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next

        small.next = blist.next
        big.next = None

        return slist.next
    
def list_to_linked(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

sol = Solution()
head = list_to_linked([1, 4, 3, 2, 5, 2])
x = 3
new_head = sol.partition(head, x)
print(linked_to_list(new_head))

print("działa")
# z pomocą Chata again...