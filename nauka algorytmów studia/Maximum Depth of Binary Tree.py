class Solution(object):
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root: 
            return 0

        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))