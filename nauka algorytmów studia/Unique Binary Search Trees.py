class Solution(object):
    def numTrees(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        unique_bst_counts = [1] * (n + 1)
        
        for total_nodes in range(2, n + 1):
            total = 0
            for root_node in range(1, total_nodes + 1):
                total += unique_bst_counts[root_node - 1] * unique_bst_counts[total_nodes - root_node]
            unique_bst_counts[total_nodes] = total
        
        return unique_bst_counts[n]
    
sol = Solution()

# Test 1
assert sol.numTrees(0) == 1

# Test 2
assert sol.numTrees(1) == 1

# Test 3
assert sol.numTrees(2) == 2

# Test 4
assert sol.numTrees(3) == 5

# Test 5
assert sol.numTrees(4) == 14

# Test 6
assert sol.numTrees(5) == 42

print("smiech")