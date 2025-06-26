from typing import Optional, List, Tuple

class TreeNode(object):
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total_sum: int = 0
        node_stack: List[Tuple[Optional[TreeNode], bool]] = [(root, False)]

        while node_stack:
            current_node, is_left_child = node_stack.pop()

            if not current_node:
                continue

            if not current_node.left and not current_node.right:
                if is_left_child:
                    total_sum += current_node.val
            else:
                node_stack.append((current_node.left, True))
                node_stack.append((current_node.right, False))

        return total_sum
    
    
