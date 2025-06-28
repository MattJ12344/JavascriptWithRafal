class Solution(object):
    def minCostClimbingStairs(self, step_costs: list[int]) -> int:
        """
        :type step_costs: List[int]
        :rtype: int
        """
        step_costs.append(0)
        
        for step_index in range(len(step_costs) - 4, -1, -1):
            step_costs[step_index] += min(step_costs[step_index + 1], step_costs[step_index + 2])

        return min(step_costs[0], step_costs[1])
    
sol = Solution()


assert sol.minCostClimbingStairs([10, 15, 20]) == 15

assert sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6

assert sol.minCostClimbingStairs([0, 0, 0, 1]) == 0

assert sol.minCostClimbingStairs([5, 5, 5, 5]) == 10


assert sol.minCostClimbingStairs([0, 0]) == 0
assert sol.minCostClimbingStairs([1, 2]) == 1
assert sol.minCostClimbingStairs([2, 1]) == 1

assert sol.minCostClimbingStairs([0, 1, 0, 1, 0, 1]) == 0

print("Nuda")