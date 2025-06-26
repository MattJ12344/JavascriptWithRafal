class Solution(object):
    def countBits(self, n: int) -> list[int]:
        """
        :type n: int
        :rtype: List[int]
        """
        bit_counts: list[int] = [0] * (n + 1)
        current_power_of_two: int = 1

        for i in range(1, n + 1):
            if current_power_of_two * 2 == i:
                current_power_of_two = i
            
            bit_counts[i] = bit_counts[i - current_power_of_two] + 1
        
        return bit_counts
    
sol = Solution()

assert sol.countBits(2) == [0, 1, 1]
assert sol.countBits(5) == [0, 1, 1, 2, 1, 2]
assert sol.countBits(0) == [0]
assert sol.countBits(1) == [0, 1]
assert sol.countBits(8) == [0, 1, 1, 2, 1, 2, 2, 3, 1]

print("Zabic")