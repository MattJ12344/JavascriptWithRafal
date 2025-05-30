class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        return self.preOrder(root,[])

    def preOrder(self,root,list) :
        if root is None: return list
        list.append(root.val)
        self.preOrder(root.left,list)
        self.preOrder(root.right,list)

        return list