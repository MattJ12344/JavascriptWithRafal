# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        leftDepth:int = self.getDepth(root.left)
        rightDepth:int = self.getDepth(root.right)
        
        if leftDepth == rightDepth:
            return (1 << leftDepth) + self.countNodes(root.right)
        else:
            return (1 << rightDepth) + self.countNodes(root.left)
    
    def getDepth(self, node: Optional[TreeNode]) -> int:
        depth:int = 0
        while node:
            depth += 1
            node = node.left
        return depth