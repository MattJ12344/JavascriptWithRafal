from typing import Optional, List

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
    
sol = Solution()

assert sol.postorderTraversal(None) == []

root1 = TreeNode(1)
assert sol.postorderTraversal(root1) == [1]

root2 = TreeNode(1)
root2.right = TreeNode(2)
root2.right.left = TreeNode(3)
assert sol.postorderTraversal(root2) == [3, 2, 1]

root3 = TreeNode(1)
root3.left = TreeNode(2, TreeNode(4), TreeNode(5))
root3.right = TreeNode(3, TreeNode(6), TreeNode(7))
assert sol.postorderTraversal(root3) == [4, 5, 2, 6, 7, 3, 1]

print("OMG!")