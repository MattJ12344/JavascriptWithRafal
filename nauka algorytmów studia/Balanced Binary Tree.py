from typing import Optional

class TreeNode(object):
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.height(root) >= 0

    def height(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        left_height: int = self.height(node.left)
        right_height: int = self.height(node.right)

        if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1
    

sol = Solution()

# Test 1
assert sol.isBalanced(None) == True

# Test 2
root = TreeNode(1)
assert sol.isBalanced(root) == True

# Test 3
root = TreeNode(1, TreeNode(2), TreeNode(3))
assert sol.isBalanced(root) == True

# Test 4
root = TreeNode(1, TreeNode(2, TreeNode(3)))
assert sol.isBalanced(root) == False

# Test 5
root = TreeNode(1,
                TreeNode(2, TreeNode(4), TreeNode(5)),
                TreeNode(3, None, TreeNode(6)))
assert sol.isBalanced(root) == True

# Test 6
root = TreeNode(1,
                TreeNode(2, TreeNode(3, TreeNode(4))),
                TreeNode(5))
assert sol.isBalanced(root) == False


print("was")