class Solution(object):
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def post(root: Optional[TreeNode], output: List[int]) -> List[int]:
            if root:
                post(root.left, output)
                post(root.right, output)
                output.append(root.val)
                
        result: List[int] = []
        
        post(root, result)
        
        return result