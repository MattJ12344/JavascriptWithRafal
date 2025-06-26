from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        :type root: Optional[TreeNode]
        :rtype: None. Modifies the tree in-place.
        """
        def inorder_traversal(node: Optional[TreeNode]) -> None:
            if not node:
                return

            inorder_traversal(node.left)

            if self.prev_node and self.prev_node.val > node.val:
                if not self.first_node:
                    self.first_node = self.prev_node
                self.second_node = node

            self.prev_node = node

            inorder_traversal(node.right)

        self.first_node: Optional[TreeNode] = None
        self.second_node: Optional[TreeNode] = None
        self.prev_node: Optional[TreeNode] = None

        inorder_traversal(root)
        if self.first_node and self.second_node:
            self.first_node.val, self.second_node.val = self.second_node.val, self.first_node.val
          
          
# TEST 1            
tree1 = TreeNode(1)
tree1.left = TreeNode(3)
tree1.left.right = TreeNode(2)

Solution().recoverTree(tree1)
assert [tree1.left.val, tree1.left.right.val, tree1.val] == [1, 2, 3]


# TEST 2
tree2 = TreeNode(3)
tree2.left = TreeNode(1)
tree2.right = TreeNode(4)
tree2.right.left = TreeNode(2)

Solution().recoverTree(tree2)
assert tree2.val == 2
assert tree2.right.left.val == 3

# TEST 3
tree3 = TreeNode(2)
tree3.left = TreeNode(1)
tree3.right = TreeNode(3)

Solution().recoverTree(tree3)
assert tree3.left.val == 1 and tree3.val == 2 and tree3.right.val == 3

print("zrobione ")