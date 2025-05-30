class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def post(root, arr):
            if root:
                post(root.left, arr)
                post(root.right, arr)
                arr.append(root.val)
        arr = []
        post(root, arr)
        return arr