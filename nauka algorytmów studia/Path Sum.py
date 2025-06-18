class Solution(object):
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        
        if not root.left and not root.right:
            return targetSum == root.val
        
        leftSum: bool = self.hasPathSum(root.left, targetSum - root.val)
        rightSum: bool = self.hasPathSum(root.right, targetSum - root.val)
        
        return leftSum or rightSum