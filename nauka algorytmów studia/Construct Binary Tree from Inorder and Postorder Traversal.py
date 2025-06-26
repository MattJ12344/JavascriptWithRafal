# Definition for a binary tree node.
from typing import Optional, List
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution(object):
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not inorder:
            return
        
        rootValue:int=postorder.pop() 
        root: Optional[TreeNode] =TreeNode(rootValue) 
        rootIndex: int =inorder.index(rootValue) 
        
        root.right=self.buildTree(inorder[rootIndex+1:],postorder) 
        root.left=self.buildTree(inorder[:rootIndex],postorder) 
        return root


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

solution = Solution()
tree_root = solution.buildTree(inorder, postorder)


assert tree_root.val == 3
assert tree_root.left.val == 9
assert tree_root.right.val == 20
assert tree_root.right.left.val == 15
assert tree_root.right.right.val == 7

print("ktosiek")