from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        self.total_tilt: int = 0

        def sum_subtree(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_sum: int = sum_subtree(node.left)
            right_sum: int = sum_subtree(node.right)
            self.total_tilt += abs(left_sum - right_sum)
            return left_sum + right_sum + node.val

        sum_subtree(root)
        return self.total_tilt
    
# Test 1
sol = Solution()
assert sol.findTilt(None) == 0

# Test 2
root = TreeNode(5)
sol = Solution()
assert sol.findTilt(root) == 0

# Test 3
root = TreeNode(1, TreeNode(2))
sol = Solution()
assert sol.findTilt(root) == 2

# Test 4
root = TreeNode(1, TreeNode(2), TreeNode(3))
sol = Solution()
assert sol.findTilt(root) == 1

# Test 5
root = TreeNode(4,
                TreeNode(2, TreeNode(3), TreeNode(5)),
                TreeNode(9, None, TreeNode(7)))
sol = Solution()
assert sol.findTilt(root) == 15

print("Nuda")