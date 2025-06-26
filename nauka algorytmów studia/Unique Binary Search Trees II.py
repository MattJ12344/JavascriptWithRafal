from typing import List, Optional
from itertools import product

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def rec(start: int, end: int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]
            if start == end:
                return [TreeNode(start)]

            all_trees: List[Optional[TreeNode]] = []

            for root_val in range(start, end + 1):
                left_subtrees = rec(start, root_val - 1)
                right_subtrees = rec(root_val + 1, end)

                for left, right in product(left_subtrees, right_subtrees):
                    all_trees.append(TreeNode(root_val, left, right))

            return all_trees

        return rec(1, n) if n > 0 else []
    

sol = Solution()

# Test 1
assert sol.generateTrees(0) == []

# Test 2
trees_n1 = sol.generateTrees(1)
assert len(trees_n1) == 1
assert trees_n1[0].val == 1
assert trees_n1[0].left is None and trees_n1[0].right is None

# Test 3
trees_n2 = sol.generateTrees(2)
assert len(trees_n2) == 2
vals_n2 = sorted([[t.val, 
                   t.left.val if t.left else None, 
                   t.right.val if t.right else None] for t in trees_n2])
assert vals_n2 == [[1, None, 2], [2, 1, None]]

# Test 4
trees_n3 = sol.generateTrees(3)
assert len(trees_n3) == 5

print("cos")