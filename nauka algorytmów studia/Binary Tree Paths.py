from typing import Optional, List

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result: List[str] = []
        
        def dfs(node: TreeNode, currentPath: str) -> None:
            if currentPath != "":
                currentPath += "->"
            currentPath += str(node.val)
            
            if not node.left and not node.right: 
                result.append(currentPath)
            if node.left: 
                dfs(node.left, currentPath)
            if node.right: 
                dfs(node.right, currentPath)
        
        if root:
            dfs(root, "") 
        
        return result

sol = Solution()

assert sol.binaryTreePaths(None) == []

root1 = TreeNode(1)
assert sol.binaryTreePaths(root1) == ["1"]

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.right = TreeNode(5)

assert sorted(sol.binaryTreePaths(root2)) == sorted(["1->2->5", "1->3"])

print("Nice")
