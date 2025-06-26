from typing import List

class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest_price: int = prices[0]
        max_profit: int = 0

        for price in prices[1:]:
            if lowest_price > price:
                lowest_price = price

            max_profit = max(max_profit, price - lowest_price)

        return max_profit
    

sol = Solution()

# Test 1
assert sol.maxProfit([7,1,5,3,6,4]) == 5

# Test 2
assert sol.maxProfit([7,6,4,3,1]) == 0

# Test 3
assert sol.maxProfit([5]) == 0

# Test 4
assert sol.maxProfit([1,2,3,4,5]) == 4

# Test 5
assert sol.maxProfit([5,4,3,2,1]) == 0

# Test 6
assert sol.maxProfit([3,2,6,5,0,3]) == 4

print("nowy")