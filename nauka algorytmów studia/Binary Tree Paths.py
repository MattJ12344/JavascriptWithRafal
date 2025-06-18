# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        result: List[str] = []
        
        def dfs(node: TreeNode, currentPath:str) -> None:
            if currentPath != "":
                currentPath += "->"
                
            currentPath += str(node.val)
            
            if not node.left and not node.right: 
                result.append(currentPath)
            if node.left: 
                dfs(node.left, currentPath)
            if node.right: 
                dfs(node.right, currentPath)
            
        dfs(root, "") 
        
        return result
        