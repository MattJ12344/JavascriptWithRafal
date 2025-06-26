from typing import List

class Solution(object):
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        n: int = len(nums)

        def generate_subsets(current: List[int], index: int) -> None:
            if index == n:
                result.append(list(current))
                return

            
            current.append(nums[index])
            generate_subsets(current, index + 1)

            
            current.pop()
            generate_subsets(current, index + 1)

        generate_subsets([], 0)
        return result
    
    
sol = Solution()

assert sorted(sol.subsets([1, 2])) == sorted([[], [1], [2], [1, 2]])
assert sorted(sol.subsets([0])) == sorted([[], [0]])
assert sorted(sol.subsets([1, 2, 3])) == sorted([
    [], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]
])
assert sol.subsets([]) == [[]]

print("Dodatki")