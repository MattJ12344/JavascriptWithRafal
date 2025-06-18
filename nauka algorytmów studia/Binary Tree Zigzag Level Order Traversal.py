# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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