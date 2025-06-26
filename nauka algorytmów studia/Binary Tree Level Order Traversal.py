from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution(object):
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result: List[List[int]] = []

        if not root:
            return result
        
        queue= deque()
        queue.append(root)
    
        while queue:
            same_level: List[int] = []

            for _ in range(len(queue)):
                node = queue.popleft()
                same_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(same_level)
        
        return result
    
sol = Solution()

assert sol.levelOrder(None) == []

root1 = TreeNode(1)
assert sol.levelOrder(root1) == [[1]]


root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.right.left = TreeNode(4)
assert sol.levelOrder(root2) == [[1], [2, 3], [4]]

print("Nuda")