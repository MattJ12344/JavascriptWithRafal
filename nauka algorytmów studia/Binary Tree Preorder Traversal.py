from typing import Optional, List

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        return self.preOrder(root,[])

    def preOrder(self,root: Optional[TreeNode],list: List[int] ) -> List[int]:
        if root is None: 
            return list
        
        list.append(root.val)
        
        self.preOrder(root.left,list)
        
        self.preOrder(root.right,list)

        return list
    
sol = Solution()

assert sol.preorderTraversal(None) == []

root1 = TreeNode(1)
assert sol.preorderTraversal(root1) == [1]


root2 = TreeNode(1)
root2.right = TreeNode(2)
root2.right.left = TreeNode(3)
assert sol.preorderTraversal(root2) == [1, 2, 3]

root3 = TreeNode(1)
root3.left = TreeNode(2, TreeNode(4), TreeNode(5))
root3.right = TreeNode(3, TreeNode(6), TreeNode(7))
assert sol.preorderTraversal(root3) == [1, 2, 4, 5, 3, 6, 7]

print("Wykoane")