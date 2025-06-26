from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result: list[int] = []
        stack: list[TreeNode] = []
        current: Optional[TreeNode] = root

        while current or stack:
            
            while current:
                stack.append(current)
                current = current.left
                
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result
    
sol = Solution()

tree1 = TreeNode(1)
tree1.right = TreeNode(2)
tree1.right.left = TreeNode(3)
assert sol.inorderTraversal(tree1) == [1, 3, 2]

assert sol.inorderTraversal(None) == []

tree2 = TreeNode(42)
assert sol.inorderTraversal(tree2) == [42]

tree3 = TreeNode(4,
    TreeNode(2, TreeNode(1), TreeNode(3)),
    TreeNode(6, TreeNode(5), TreeNode(7))
)
assert sol.inorderTraversal(tree3) == [1, 2, 3, 4, 5, 6, 7]

print("DWA")