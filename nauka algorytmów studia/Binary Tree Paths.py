# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        res = []
        
        def dfs(node, s):
            if s != "":
                s += "->"
            s += str(node.val)
            if not node.left and not node.right: res.append(s)
            if node.left: dfs(node.left, s)
            if node.right: dfs(node.right, s)
        dfs(root, "") 
        return res
        