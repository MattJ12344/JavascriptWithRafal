from typing import List, Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def nextPermutation(self, numbers: List[int]) -> None:
        index: int = len(numbers) - 2

        while index >= 0 and numbers[index] >= numbers[index + 1]:
            index -= 1

        if index >= 0:
            j = len(numbers) - 1
            while numbers[j] <= numbers[index]:
                j -= 1
            numbers[index], numbers[j] = numbers[j], numbers[index]

        numbers[index + 1:] = reversed(numbers[index + 1:])

    def partition(self, head: ListNode, x: int) -> ListNode:
        slist = ListNode()
        blist = ListNode()
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

# Test
a = ListNode(1)
b = ListNode(4)
c = ListNode(3)
d = ListNode(2)
e = ListNode(5)
f = ListNode(2)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

sol = Solution()
res = sol.partition(a, 3)

assert res.val == 1
assert res.next.val == 2
assert res.next.next.val == 2
assert res.next.next.next.val == 4
assert res.next.next.next.next.val == 3
assert res.next.next.next.next.next.val == 5
assert res.next.next.next.next.next.next is None

print("Kod  ")