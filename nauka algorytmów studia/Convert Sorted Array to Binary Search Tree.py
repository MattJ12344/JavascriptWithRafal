class Solution(object):
    def sortedArrayToBST(self, numbers: list[int]) -> Optional[TreeNode]:
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        totalNumbers:int = len(numbers)
        if not totalNumbers:
            return None

        midNode:int = totalNumbers // 2
        
        return TreeNode(
            numbers[midNode], 
            self.sortedArrayToBST(numbers[:midNode]), self.sortedArrayToBST(numbers[midNode + 1 :])
        )