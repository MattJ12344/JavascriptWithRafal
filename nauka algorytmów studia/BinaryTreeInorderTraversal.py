class Solution(object):
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result: list[int] = []
        stack: list[TreeNode] = []
        current: Optional[TreeNode] = root

        while current or stack:
            
            while current:
                stack.append(current)
                current = current.left
                
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result