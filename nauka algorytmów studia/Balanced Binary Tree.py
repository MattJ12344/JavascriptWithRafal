class Solution(object):
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return (self.Height(root) >= 0)
    
    def Height(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:  
            return 0
        
        leftHeight: int = self.Height(root.left) 
        rightHeight: int =  self.Height(root.right)
        
        if leftHeight < 0 or rightHeight < 0 or abs(leftHeight - rightHeight) > 1:  
            return -1
        
        return max(leftHeight, rightHeight) + 1