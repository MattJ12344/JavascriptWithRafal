# Definition for a binary tree node.
from typing import Optional
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution(object):
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return root

        tempTree: Optional[TreeNode] = root.left
        root.left = root.right
        root.right = tempTree

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

inverted = Solution().invertTree(root)

assert inverted.val == 4
assert inverted.left.val == 7
assert inverted.right.val == 2
assert inverted.left.left.val == 9
assert inverted.left.right.val == 6
assert inverted.right.left.val == 3
assert inverted.right.right.val == 1

root = TreeNode(1)
inverted = Solution().invertTree(root)
assert inverted.val == 1
assert inverted.left is None
assert inverted.right is None

root = TreeNode(1)
root.left = TreeNode(2)
inverted = Solution().invertTree(root)
assert inverted.val == 1
assert inverted.left is None
assert inverted.right.val == 2

assert Solution().invertTree(None) is None

print("Widze")