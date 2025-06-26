from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root: 
            return 0

        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    

sol = Solution()

# Test 1
assert sol.maxDepth(None) == 0

# Test 2
assert sol.maxDepth(TreeNode(1)) == 1

# Test 3
tree = TreeNode(1)
tree.left = TreeNode(2, TreeNode(4))
tree.right = TreeNode(3)
assert sol.maxDepth(tree) == 3

# Test 4
tree = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
assert sol.maxDepth(tree) == 4

print("Nuda")