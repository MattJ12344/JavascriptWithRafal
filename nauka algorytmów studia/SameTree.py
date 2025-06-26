from typing import Optional

class TreeNode(object):
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        """
        :type node1: Optional[TreeNode]
        :type node2: Optional[TreeNode]
        :rtype: bool
        """
        if not node1 and not node2:
            return True
        if not node1 or not node2 or node1.val != node2.val:
            return False
        return self.isSameTree(node1.left, node2.left) and self.isSameTree(node1.right, node2.right)
    
sol = Solution()

# 
t1 = TreeNode(1)
t2 = TreeNode(1)
assert sol.isSameTree(t1, t2) == True

# 
a1 = TreeNode(1, TreeNode(2), TreeNode(3))
a2 = TreeNode(1, TreeNode(2), TreeNode(3))
assert sol.isSameTree(a1, a2) == True

#
b1 = TreeNode(1, TreeNode(2))
b2 = TreeNode(1, None, TreeNode(2))
assert sol.isSameTree(b1, b2) == False

# 
c1 = TreeNode(1, TreeNode(2), TreeNode(1))
c2 = TreeNode(1, TreeNode(1), TreeNode(2))
assert sol.isSameTree(c1, c2) == False

# 
assert sol.isSameTree(None, None) == True

print("Proba")