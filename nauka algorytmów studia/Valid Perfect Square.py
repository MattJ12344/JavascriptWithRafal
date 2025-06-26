class Solution(object):
    def isPerfectSquare(self, number: int) -> bool:
        """
        :type number: int
        :rtype: bool
        """
        if number < 2:
            return True

        left: int = 2
        right: int = number // 2

        while left <= right:
            mid: int = (left + right) // 2
            squared: int = mid * mid

            if squared == number:
                return True
            elif squared < number:
                left = mid + 1
            else:
                right = mid - 1

        return False
    
sol = Solution()

# Test 1
assert sol.isPerfectSquare(16) == True

# Test 2
assert sol.isPerfectSquare(14) == False

# Test 3
assert sol.isPerfectSquare(0) == True

# Test 4
assert sol.isPerfectSquare(1) == True

# Test 5
assert sol.isPerfectSquare(100000000) == True

# Test 6
assert sol.isPerfectSquare(26) == False

# Test 7
assert sol.isPerfectSquare(81) == True

# Test 8
assert sol.isPerfectSquare(80) == False

print("pies")