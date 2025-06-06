# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        
        cos = collections.deque()
        cos.append(root)

        while cos:
            same_level = []

            for _ in range(len(cos)):
                node = cos.popleft()
                same_level.append(node.val)

                if node.left:
                    cos.append(node.left)
                if node.right:
                    cos.append(node.right)
            
            result.append(same_level)
        
        return result