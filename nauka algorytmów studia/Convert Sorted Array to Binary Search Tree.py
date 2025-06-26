from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, numbers: List[int]) -> Optional[TreeNode]:
        """
        :type numbers: List[int]
        :rtype: Optional[TreeNode]
        """
        if not numbers:
            return None

        midNode: int = len(numbers) // 2
        
        return TreeNode(
            numbers[midNode], 
            self.sortedArrayToBST(numbers[:midNode]), 
            self.sortedArrayToBST(numbers[midNode + 1:])
        )

sol = Solution()
tree_root = sol.sortedArrayToBST([-10, -3, 0, 5, 9])

assert tree_root.val == 0
assert tree_root.left.val == -3
assert tree_root.left.left.val == -10
assert tree_root.right.val == 9
assert tree_root.right.left.val == 5

print("Mosiek")