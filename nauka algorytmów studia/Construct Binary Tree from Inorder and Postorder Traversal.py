# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not inorder:
            return
        
        rootValue:int=postorder.pop() 
        root: Treenode =TreeNode(rootValue) 
        rootIndex: int =inorder.index(rootValue) 
        
        root.right=self.buildTree(inorder[rootIndex+1:],postorder) 
        root.left=self.buildTree(inorder[:rootIndex],postorder) 
        return root
