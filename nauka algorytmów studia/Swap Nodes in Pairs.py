from typing import Optional

class ListNode(object):
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nodeHead: ListNode = ListNode(0, head)

        previousNode: ListNode = nodeHead
        currentNode: Optional[ListNode] = head

        while currentNode and currentNode.next:
            nextPairStart: Optional[ListNode] = currentNode.next.next
            secondNode: ListNode = currentNode.next

            secondNode.next = currentNode
            currentNode.next = nextPairStart
            previousNode.next = secondNode

            previousNode = currentNode
            currentNode = nextPairStart

        return nodeHead.next
    
sol = Solution()


n1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
out1 = sol.swapPairs(n1)
assert [out1.val, out1.next.val, out1.next.next.val, out1.next.next.next.val] == [2, 1, 4, 3]

# Test 2
n2 = ListNode(1)
out2 = sol.swapPairs(n2)
assert out2.val == 1 and out2.next is None

# Test 3
out3 = sol.swapPairs(None)
assert out3 is None

# Test 4
n4 = ListNode(1, ListNode(2, ListNode(3)))
out4 = sol.swapPairs(n4)
assert [out4.val, out4.next.val, out4.next.next.val] == [2, 1, 3]

# Test 5
n5 = ListNode(100, ListNode(200))
out5 = sol.swapPairs(n5)
assert [out5.val, out5.next.val] == [200, 100]

# Test 6
n6 = ListNode(1)
p = n6
for i in range(2, 11):
    p.next = ListNode(i)
    p = p.next
out6 = sol.swapPairs(n6)
vals6 = []
while out6:
    vals6.append(out6.val)
    out6 = out6.next
assert vals6 == [2,1,4,3,6,5,8,7,10,9]

print("lubie")