# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        def rec(start, end):
		
            if start > end:
                return [None]
				
            if start == end:
                return [TreeNode(start)]
            ret_list = []
			
            for i in range(start, end+1):
                left = rec(start, i-1)
                right = rec(i+1, end)
                for pair in product(left, right):
                    ret_list.append(TreeNode(i, pair[0], pair[1]))
        
            return ret_list
        
        result = rec(1,n)
        return result