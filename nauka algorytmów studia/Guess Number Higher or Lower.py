def guess(picked_number: int) -> int:
    if picked_number > secret:
        return -1
    elif picked_number < secret:
        return 1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            middle = (left + right) // 2
            result = guess(middle)

            if result == 0:
                return middle
            elif result == -1:
                right = middle - 1
            else:
                left = middle + 1

        return -1  



sol = Solution()

# Test 1
secret = 6
assert sol.guessNumber(10) == 6

# Test 2
secret = 1
assert sol.guessNumber(1) == 1

# Test 3
secret = 2
assert sol.guessNumber(2) == 2

# Test 4 
secret = 42
assert sol.guessNumber(100) == 42

print("NuDa")