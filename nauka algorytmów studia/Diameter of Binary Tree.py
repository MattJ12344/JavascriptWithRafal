from typing import Optional, List

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        def diameter(node: Optional[TreeNode], result: List[int]) -> int:
            if not node:
                return 0
            
            left = diameter(node.left, result)
            right = diameter(node.right, result)

            result[0] = max(result[0], left + right)

            return max(left, right) + 1
        
        result: List[int] = [0]
        diameter(root, result)
        return result[0]
    
sol = Solution()

assert sol.diameterOfBinaryTree(None) == 0

assert sol.diameterOfBinaryTree(TreeNode(1)) == 0

n3 = TreeNode(3)
n2 = TreeNode(2, None, n3)
n1 = TreeNode(1, None, n2)
assert sol.diameterOfBinaryTree(n1) == 2

n3 = TreeNode(3)
n2 = TreeNode(2, n3)
n1 = TreeNode(1, n2)
assert sol.diameterOfBinaryTree(n1) == 2

root = TreeNode(1,
                TreeNode(2, TreeNode(4), TreeNode(5)),
                TreeNode(3))
assert sol.diameterOfBinaryTree(root) == 3

root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
assert sol.diameterOfBinaryTree(root) == 3


print("Nuda")