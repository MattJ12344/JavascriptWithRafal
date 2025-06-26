from typing import List

class Solution(object):
    def findPoisonedDuration(self, attack_times: List[int], duration: int) -> int:
        """
        :type attack_times: List[int]
        :type duration: int
        :rtype: int
        """
        total_poisoned_time = 0
        num_attacks = len(attack_times)

        for i in range(num_attacks - 1):
            time_between_attacks = attack_times[i + 1] - attack_times[i]
            total_poisoned_time += duration if time_between_attacks > duration else time_between_attacks

        return total_poisoned_time + (duration if num_attacks else 0)
    
    
s = Solution()

# Test 1
assert s.findPoisonedDuration([1, 4], 2) == 4    


assert s.findPoisonedDuration([10, 20, 30], 5) == 15 

# Test 2
assert s.findPoisonedDuration([1, 2], 2) == 3    


assert s.findPoisonedDuration([1, 2, 3], 2) == 4  

# Test 3
assert s.findPoisonedDuration([5], 10) == 10

# Test 4
assert s.findPoisonedDuration([], 3) == 0

# Test 5
assert s.findPoisonedDuration([1, 5, 6], 1000000) == 1000005

print("ja")