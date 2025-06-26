from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result:  list[list[int]]  = []
        queue: list[TreeNode] = deque([root])
        isLeftToRight: bool = True

        while queue:
            level_size = len(queue)
            current_level:list[int] = [0] * level_size

            for i in range(level_size):
                node = queue.popleft()
                index = i if isLeftToRight else level_size - 1 - i
                current_level[index] = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)
            isLeftToRight = not isLeftToRight

sol = Solution()


tree1 = TreeNode(3)
tree1.left = TreeNode(9)
tree1.right = TreeNode(20)
tree1.right.left = TreeNode(15)
tree1.right.right = TreeNode(7)

assert sol.zigzagLevelOrder(tree1) == [[3], [20, 9], [15, 7]]

assert sol.zigzagLevelOrder(None) == []

tree2 = TreeNode(1)
assert sol.zigzagLevelOrder(tree2) == [[1]]

tree3 = TreeNode(1)
tree3.left = TreeNode(2)
tree3.right = TreeNode(3)
assert sol.zigzagLevelOrder(tree3) == [[1], [3, 2]]

tree4 = TreeNode(1)
tree4.left = TreeNode(2, TreeNode(4))
tree4.right = TreeNode(3, None, TreeNode(5))
assert sol.zigzagLevelOrder(tree4) == [[1], [3, 2], [4, 5]]

print("Nuda")